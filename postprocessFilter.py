import pickle


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
    shingles=getShingles()
    pairwise_similarity_map = dict()
    for pair in pairs:
        doc1=shingles[pair[0]]
        doc2 = shingles[pair[1]]
        union=doc1.union(doc2)
        intersect = doc1.intersection(doc2)
        jaccard_sim = len(intersect) / len(union)
        pairwise_similarity_map[pair] = jaccard_sim
    with open('obj/candidate_pair_jacard.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)


if __name__=="__main__":
    main()