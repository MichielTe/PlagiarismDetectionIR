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
        # For actual jaccard similarity
        union=doc1.union(doc2)
        intersect = doc1.intersection(doc2)
        jaccard_sim = len(intersect) / len(union)
        # For approximated jaccard
        # simcounter = 0
        # for i in range(len(doc1)):
        #     if doc1[i] == doc2[i]:
        #         simcounter += 1
        # jaccard_sim = simcounter / len(doc1)
        if jaccard_sim >= threshold:
            true_positives += 1
        else:
            false_positives += 1
        pairwise_similarity_map[pair] = jaccard_sim
    print("total number true positives: ", true_positives)
    print("total number false positives: ", false_positives)
    with open('obj/candidate_pair_jacard.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)

    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = ['doc_id1', 'doc_id2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pair in pairwise_similarity_map:
            if(pairwise_similarity_map[pair]>0.8):
                writer.writerow({"doc_id1":pair[0],"doc_id2":pair[1]})



if __name__=="__main__":
    main()