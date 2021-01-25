import pickle
import math
from hashFunctions import generateHashFunctions, LSH_hash

def getData():
    with open('obj/shingles.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


def createSignatureMatrix(data, nb_hashes):
    signature_matrix = []
    hashes = generateHashFunctions(nb_hashes)
    for row in data:
        signature_row = [math.inf]*nb_hashes
        for shingle in row:
            for hash_i in range(nb_hashes):
                rotations, XORvalue = hashes[hash_i]
                signature_row[hash_i] = min(signature_row[hash_i], LSH_hash(shingle, rotations, XORvalue))
        signature_matrix.append(signature_row)
    with open('obj/signature_matrix.pkl', 'wb') as file:
        pickle.dump(signature_matrix, file)
    return signature_matrix

data = getData()
test = createSignatureMatrix(data, 100)
