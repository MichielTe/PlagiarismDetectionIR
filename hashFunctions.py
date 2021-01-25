import sys
import random
import hashlib

# MAX_INT = sys.maxsize
# INT_BITS = sys.getsizeof(MAX_INT)
# BYTES_SLICED = int((INT_BITS) / 8)
INT_SIZE = 32
INT_SIZE_BYTES = 4

def generateHashFunctions(n):
    hashFunction = []
    for i in range(n):
        #random_XORvalue = random.randint(-sys.maxsize, sys.maxsize)
        random_XORvalue = random.getrandbits(INT_SIZE)
        random_rotations = random.randint(0, INT_SIZE-1)
        hashFunction.append((random_rotations, random_XORvalue))
    return hashFunction


def leftRotate(n, d):
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d) | (n >> (INT_SIZE - d))


def LSH_hash(value, rotations, XORvalue):
    #new_value = hashlib.sha1(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_value = hashlib.md5(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_int_value = int.from_bytes(new_value, 'big')
    return leftRotate(new_int_value, rotations) ^ XORvalue
