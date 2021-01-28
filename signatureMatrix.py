import math
import pickle

from hashFunctions import generateHashFunctions, LSH_hash


def getData():
    # Gets the shingles documents from previous step in the process (shingles.py file)
    with open('obj/shingles.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


def createSignature(data_row, hashes):
    """
    Creates the signature for a single document
    :param data_row: A document being represented by shingles
    :param hashes: the list of hashes needed to create the signature (size M)
    :return: a signature of the given document
    """
    nb_hashes = len(hashes)
    signature_row = [math.inf] * nb_hashes
    for shingle in data_row:
        for hash_i in range(nb_hashes):
            XORvalue = hashes[hash_i]
            signature_row[hash_i] = min(signature_row[hash_i], LSH_hash(shingle, XORvalue))
    return signature_row


def createSignatureMatrix(data, hashes):
    """
    This function creates a len(data)*len(hashes) signature matrix by hashing all shingles with each hashfunction
    Then it stores the lowest value gotten per hashfunction per document as a single row
    This is the sketching process of the LSH algorithm
    :param data: The shingled documents
    :param hashes: The list of hashes
    :return: A signature matrix
    """
    signature_matrix = []
    nb_hashes = len(hashes)
    for row in data:
        signature_matrix.append(createSignature(row, hashes))
    with open('obj/signature_matrix.pkl', 'wb') as file:
        pickle.dump(signature_matrix, file)
    return signature_matrix


if __name__ == "__main__":
    data = getData()
    # Generate M hash functions to create the signatures
    hashFunctions = generateHashFunctions(100)
    test = createSignatureMatrix(data, hashFunctions)
    with open('obj/used_hashes.pkl', 'wb') as file:
        pickle.dump(hashFunctions, file)
