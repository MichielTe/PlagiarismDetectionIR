import pickle
import csv

def getShingles():
    with open('obj/shingles.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def getBuckets():
    with open('obj/buckets.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def create_candidate_pairs():
    """
    This function goes over all buckets and creates unique candidate pairs for each bucket with more than 2 entries
    Here we make sure that we also don't get both (A,B) and (B,A) as candidate pair, hence the nestedness
    :return: A list of candidate pairs
    """
    buckets = getBuckets()
    candidate_pairs = set()
    for band in buckets:
        for val, bucket in band.items():
            if len(bucket) > 1:
                for docid1 in bucket:
                    for docid2 in bucket:
                        if (docid1 is not docid2):
                            doc1 = min(docid1, docid2)
                            doc2 = max(docid1, docid2)
                            candidate_pairs.add((doc1, doc2))
    return candidate_pairs

def main():
    """
    This main function will go over the filled buckets, and will first create the candidate pairs
    Then it will calculate the actual jaccard similarity per document and check whether all pairs have the needed similarity
    This is to remove false positives, which actually don't occur in both datasets for this project, as the signature sizes and band were chose accordingly
    :return:
    """
    pairs=create_candidate_pairs()
    print("total number of candidate pairs: ", len(pairs))
    shingles=getShingles()
    pairwise_similarity_map = dict()
    false_positives = 0
    true_positives = 0
    threshold = 0.8
    for pair in pairs:
        doc1=shingles[pair[0]]
        doc2 = shingles[pair[1]]
        # calculate jaccard similarity
        union=doc1.union(doc2)
        intersect = doc1.intersection(doc2)
        jaccard_sim = len(intersect) / len(union)
        # Simple diagnostic counter
        if jaccard_sim >= threshold:
            true_positives += 1
        else:
            false_positives += 1
        pairwise_similarity_map[pair] = jaccard_sim
    print("total number true positives: ", true_positives)
    print("total number false positives: ", false_positives)

    # Dump similarities to separate file for graphing
    with open('obj/candidate_pair_jacard.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)

    # Dump candidate pairs to csv file
    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = ['doc_id1', 'doc_id2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pair in pairwise_similarity_map:
            if(pairwise_similarity_map[pair]>0.8):
                writer.writerow({"doc_id1":pair[0],"doc_id2":pair[1]})



if __name__=="__main__":
    main()