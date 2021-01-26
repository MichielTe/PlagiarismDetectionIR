import pickle
import math
from hashFunctions import generateHashFunctions, LSH_hash

def getData():
    with open('obj/shingles.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


def createSignature(data_row, hashes):
    nb_hashes = len(hashes)
    signature_row = [math.inf] * nb_hashes
    for shingle in data_row:
        for hash_i in range(nb_hashes):
            rotations, XORvalue = hashes[hash_i]
            signature_row[hash_i] = min(signature_row[hash_i], LSH_hash(shingle, rotations, XORvalue))
    return signature_row


def createSignatureMatrix(data, hashes):
    signature_matrix = []
    nb_hashes = len(hashes)
    for row in data:
        signature_matrix.append(createSignature(row, hashes))
    with open('obj/signature_matrix.pkl', 'wb') as file:
        pickle.dump(signature_matrix, file)
    return signature_matrix


if __name__ == "__main__":
    data = getData()
    hashFunctions = generateHashFunctions(100)
    test = createSignatureMatrix(data, hashFunctions)
    with open('obj/used_hashes.pkl', 'wb') as file:
        pickle.dump(hashFunctions, file)
