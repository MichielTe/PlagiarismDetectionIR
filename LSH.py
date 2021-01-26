import pickle


def LSH(signature_row, nb_bands):
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
    M = len(signature_matrix[0])
    if M % nb_bands != 0:
        print("please pick a 'b' value for which M%b equals zero")
        return
    bucket_list = [dict() for i in range(nb_bands)]
    for i in range(len(signature_matrix)):
        buckets = LSH(signature_matrix[i], nb_bands)
        for j, bucket in enumerate(buckets):
            band_buckets = bucket_list[j]
            if bucket in band_buckets:
                band_buckets[bucket].add(i)
            else:
                band_buckets[bucket] = {i}
    return bucket_list


with open('obj/signature_matrix.pkl', 'rb') as file:
    data = pickle.load(file)

test = LSHCreateBuckets(data, 20)
print(test)
