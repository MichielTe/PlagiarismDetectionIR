import pickle

def getData():
    with open('obj/signature_matrix.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    """
    This function is used to approximate the jaccard index and dump the data in such a way that it can be used in the similarityGraph.py file
    This function can only be run if you already have a signature matrix with minhash signatures of the documents
    This can be quite computationally expensive, especially with the large dataset
    :return:
    """
    pairwise_similarity_map=dict()
    data = getData()
    for outer_doc_counter in range(len(data)):
        outer_set=data[outer_doc_counter]
        for inner_doc_counter in range(outer_doc_counter+1,len(data)):
            inner_set = data[inner_doc_counter]
            # The counter that counts the amount of minhashes being equal
            simcounter=0
            for i in range(len(outer_set)):
                if outer_set[i]==inner_set[i]:
                    simcounter+=1
            # Approc jaccard = #equal minshashes/len(signature)
            jaccard_sim=simcounter/len(outer_set)
            pairwise_similarity_map[(outer_doc_counter,inner_doc_counter)]=jaccard_sim
    # Dump it to file that can be used in the graph file
    with open('obj/similarityApprox.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)

if __name__ == "__main__":
    main()