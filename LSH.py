import pickle


def LSH(signature_row, nb_bands):
    """
    Applies the LSH algorithm for a single documents/signature
    So here this signature will be divided into "nb_bands" of M/nb_bands rows
    Keep in mind that the signature matrix is the transpos of the one seen in the course
    This is why going row by row is more efficient here
    :param signature_row: the signature of a document
    :param nb_bands: the amount of bands this document will be partitioned into
    :return:the buckets created for this signature
    """
    M = len(signature_row)
    if M % nb_bands != 0:
        print("please pick a 'b' value for which M%b equals zero")
        return
    r = int(M/nb_bands)
    buckets = []
    for i in range(nb_bands):
        band_bucket = []
        for j in range(i*r, (i+1)*r):
            band_bucket.append(signature_row[j])
        buckets.append(tuple(band_bucket))
    return buckets


def LSHCreateBuckets(signature_matrix, nb_bands):
    """
    This function maps the signature matrix to a bunch of bands per bucket
    The amount of buckets per band will be variable based on the amount of distinct hash values
    :param signature_matrix: the signature matrix
    :param nb_bands: the amount of bands
    :return: a list of filled buckets
    """
    # Get the signature size
    M = len(signature_matrix[0])
    # Quick pre condition check
    if M % nb_bands != 0:
        print("please pick a 'b' value for which M%b equals zero")
        return
    # Create all needed bucket dictionaries for LSH algorithm
    bucket_list = [dict() for i in range(nb_bands)]
    for i in range(len(signature_matrix)):
        # Perform LSH for a single row
        buckets = LSH(signature_matrix[i], nb_bands)
        # Merge results of the single row LSH with the other rows
        for j, bucket in enumerate(buckets):
            band_buckets = bucket_list[j]
            if bucket in band_buckets:
                band_buckets[bucket].add(i)
            else:
                band_buckets[bucket] = {i}
    return bucket_list


if __name__ == "__main__":
    # Load in file created by the "signatureMatrix.py" file
    with open('obj/signature_matrix.pkl', 'rb') as file:
        data = pickle.load(file)

    buckets = LSHCreateBuckets(data, 63)
    # Write output to buckets.pkl
    with open('obj/buckets.pkl', 'wb') as file:
        pickle.dump(buckets, file)
    print(buckets)
