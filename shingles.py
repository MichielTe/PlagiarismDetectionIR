import pickle
def getData():
    with open('obj/documents.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def create_shingles(data, k):
    shingle_dict = dict()
    new_shingle_data = list()
    counter = 0
    for row in data:
        rowLen = len(row)
        dataSet = set()
        for i in range(rowLen):
            shingle = ""
            end = False
            for j in range(i, i+k):
                if j < rowLen:
                    shingle += ' ' + row[j]
                else:
                    end = True
                    break
            if end:
                break
            if shingle in shingle_dict:
                dataSet.add(shingle_dict[shingle])
            else:
                shingle_dict[shingle] = counter
                dataSet.add(counter)
                counter+=1
        new_shingle_data.append(dataSet)
    return new_shingle_data, shingle_dict


if __name__ == "__main__":
    data = getData()
    new_shingle_data, shingles_dict = create_shingles(data, 8)
    with open('obj/shingles.pkl', 'wb') as file:
        pickle.dump(new_shingle_data, file)

    with open('obj/shingles_dict.pkl', 'wb') as file:
        pickle.dump(shingles_dict, file)
