import pickle

def getData():
    with open('obj/signature_matrix.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    pairwise_similarity_map=dict()
    data = getData()
    for outer_doc_counter in range(len(data)):
        outer_set=data[outer_doc_counter]
        for inner_doc_counter in range(outer_doc_counter+1,len(data)):
            inner_set = data[inner_doc_counter]
            simcounter=0
            for i in range(len(outer_set)):
                if outer_set[i]==inner_set[i]:
                    simcounter+=1
            jaccard_sim=simcounter/len(outer_set)
            pairwise_similarity_map[(outer_doc_counter,inner_doc_counter)]=jaccard_sim
    with open('obj/similarityApprox.pkl', 'wb') as file:
        pickle.dump(pairwise_similarity_map, file)
    return 0

if __name__ == "__main__":
    main()