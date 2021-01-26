import shingles
import pickle
from signatureMatrix import createSignatureMatrix
from hashFunctions import generateHashFunctions
from LSH import LSHCreateBuckets

if __name__ == "__main__":
    save_files = False
    signature_size = 100
    number_of_bands = 20

    with open('obj/documents.pkl', 'rb') as file:
        data = pickle.load(file)
    shingle_data, shingle_dict = shingles.create_shingles(data, 2)
    hashFunctions = generateHashFunctions(signature_size)
    signature_matrix = createSignatureMatrix(shingle_data, hashFunctions)
    mapped_buckets = LSHCreateBuckets(signature_matrix, number_of_bands)
    if save_files:
        with open('obj/shingles.pkl', 'wb') as file:
            pickle.dump(shingle_data, file)
        with open('obj/used_hashes.pkl', 'wb') as file:
            pickle.dump(hashFunctions, file)
        with open('obj/signature_matrix.pkl', 'wb') as file:
            pickle.dump(signature_matrix, file)
        with open('obj/buckets.pkl', 'wb') as file:
            pickle.dump(mapped_buckets, file)

    print("done")