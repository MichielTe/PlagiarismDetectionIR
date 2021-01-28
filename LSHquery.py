import pickle
import random
import matplotlib.pyplot as plt
from signatureMatrix import createSignature
from LSH import LSH


def create_plagiarised_document(shingles, similarity):
    percent_changed = (1-similarity)/(1+similarity)
    new_doc = set({})
    doc_id = random.randint(0, len(shingles)-1)
    plagiarised = shingles[doc_id]
    copied = 0
    for gram in plagiarised:
        if random.uniform(0, 1) >= percent_changed:
            new_doc.add(gram)
            copied += 1
        else:
            new_doc.add(random.randint(0, 2044525))
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

    number_of_bands = len(buckets)
    probability_map = []
    for s in range(5, 105, 5):
        print("testing for similarity:", s)
        matches = 0
        for j in range(100):
            doc = create_plagiarised_document(shingles, s/100)
            doc_signature = createSignature(doc, used_hashes)
            mapped_buckets = LSH(doc_signature, number_of_bands)
            pairs = set({})
            for i in range(number_of_bands):
                mapped_bucket = mapped_buckets[i]
                if mapped_bucket in buckets[i]:
                    for doc in buckets[i][mapped_bucket]:
                        pairs.add(doc)
            if len(pairs) > 0:
                matches += 1
        probability_map.append(matches)
        print("number of matches found: ", matches)

    names = [str(x) for x in range(5, 105, 5)]
    fig, ax = plt.subplots()
    for idx, i in enumerate(probability_map):
        b = ax.bar(names[idx], i, 1)

    ax.set_xlabel('similarity (%)')
    ax.set_ylabel('Number of documents matched out of 100 documents')
    plt.title("Number of documents matched according to similarity ")
    plt.show()
