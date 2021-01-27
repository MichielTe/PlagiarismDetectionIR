import sys
import random
import hashlib

# MAX_INT = sys.maxsize
# INT_BITS = sys.getsizeof(MAX_INT)
# BYTES_SLICED = int((INT_BITS) / 8)
INT_SIZE = 32
INT_SIZE_BYTES = 4
# INT_MAX_VAL=math.pow(2,INT_SIZE)

def generateHashFunctions(n):
    hashFunction = []
    for i in range(n):
        #random_XORvalue = random.randint(-sys.maxsize, sys.maxsize)
        random_XORvalue = random.getrandbits(INT_SIZE)
        # random_rotations = random.randint(0, INT_SIZE-1)
        hashFunction.append((random_XORvalue))
    return hashFunction


def LSH_hash(value, XORvalue):
    #new_value = hashlib.sha1(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_value = hashlib.md5(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_int_value = int.from_bytes(new_value, 'big')
    # return new_int_value ^ XORvalue
    return new_int_value ^ XORvalue

# if __name__ == "__main__":
#     leftRotate(99654,8)
