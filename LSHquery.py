import pickle
import random
from signatureMatrix import createSignature
from LSH import LSH


def create_plagiarised_document(shingles, similarity):
    new_doc = set({})
    doc_id = random.randint(0, len(shingles)-1)
    print("plagiarised doc: ", doc_id)
    plagiarised = shingles[doc_id]
    print("len doc: ", len(plagiarised))
    copied = 0
    for gram in plagiarised:
        if random.uniform(0, 1) <= similarity:
            new_doc.add(gram)
            copied += 1
        else:
            new_doc.add(random.randint(0, 2044525))
    print("actual similarity: ", copied/len(plagiarised))
    return new_doc


if __name__ == "__main__":

    with open('obj/shingles.pkl', 'rb') as file:
        shingles = pickle.load(file)

    with open('obj/buckets.pkl', 'rb') as file:
        buckets = pickle.load(file)

    with open('obj/used_hashes.pkl', 'rb') as file:
        used_hashes = pickle.load(file)

    max_shingle = 0
    for shingle in shingles:
        max_temp = max(shingle)
        max_shingle = max(max_shingle, max_temp)
    print("highest shingle id: ", max_shingle)

    similarity = 0.80
    number_of_bands = len(buckets)
    doc = create_plagiarised_document(shingles, similarity)
    doc_signature = createSignature(doc, used_hashes)
    mapped_buckets = LSH(doc_signature, number_of_bands)
    pairs = set({})
    for i in range(number_of_bands):
        mapped_bucket = mapped_buckets[i]
        if mapped_bucket in buckets[i]:
            for doc in buckets[i][mapped_bucket]:
                pairs.add(doc)

    print(pairs)
