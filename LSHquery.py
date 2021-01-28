import pickle
import random
import matplotlib.pyplot as plt
from signatureMatrix import createSignature
from LSH import LSH

# This file is created to test our implementation
# It uses the dump files created in shingles.py, SignamtureMAtrix.py andthe LSH.py files
# The way we test our implementation is to create a documents that has similarity s with another document
# We then make a signature of said document and run it trough the LSH algorithm to see if it produces a candidate pair or not
# This is done a given amount of times for each given similarity band in the main function, so we can graph the result
# This file is used in the implementation evaluation part of the report

def create_plagiarised_document(shingles, similarity):
    """
    Creates a documents that is somewhat equal to the given shingle list, the amount it is equal is give
    :param shingles: The shingle list (preferably representing another document)
    :param similarity: The similarty that the result will have with the given shingle list
    :return: a list of shingles equal to the given shingles with given similarity
    """
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

    # Load in needed data
    with open('obj/shingles.pkl', 'rb') as file:
        shingles = pickle.load(file)

    with open('obj/buckets.pkl', 'rb') as file:
        buckets = pickle.load(file)

    with open('obj/used_hashes.pkl', 'rb') as file:
        used_hashes = pickle.load(file)

    # Simple test to see the shingle range
    max_shingle = 0
    for shingle in shingles:
        max_temp = max(shingle)
        max_shingle = max(max_shingle, max_temp)
    print("highest shingle id: ", max_shingle)

    number_of_bands = len(buckets)
    probability_map = []
    #goes over all similarity ranges
    for s in range(5, 105, 5):
        print("testing for similarity:", s)
        matches = 0
        # Makes 100 random tests per similarity range
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

    # Graph creation
    names = [str(x) for x in range(5, 105, 5)]
    fig, ax = plt.subplots()
    for idx, i in enumerate(probability_map):
        b = ax.bar(names[idx], i, 1)

    ax.set_xlabel('similarity (%)')
    ax.set_ylabel('Number of documents matched out of 100 documents')
    plt.title("Number of documents matched according to similarity ")
    plt.show()
