import pickle

def getData():
    with open('obj/shingles.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    """
    Calculates the actual jaccard index per document and dumps it in a file that can be used in the similarityGraph.py file
    This function can only be run if the documents have already been shingled
    :return:
    """
    pairwise_similarity_map=dict()
    data = getData()
    # The truepositives counter is only used for diagnostics
    TruePositives = 0
    for outer_doc_counter in range(len(data)):
        outer_set=data[outer_doc_counter]
        for inner_doc_counter in range(outer_doc_counter+1,len(data)):
            inner_set = data[inner_doc_counter]
            # Jaccard(A,B)=len(intersect(A,B))/len(Union(A,B)
            union=outer_set.union(inner_set)
            intersect=outer_set.intersection(inner_set)
            jaccard_sim=len(intersect)/len(union)
            if jaccard_sim >= 0.8:
                TruePositives += 1
            pairwise_similarity_map[(outer_doc_counter,inner_doc_counter)]=jaccard_sim
    # Dump data to file that can be used in the graph file
    with open('obj/similarity.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)
    print("True positives: ", TruePositives)
    return 0

if __name__ == "__main__":
    main()