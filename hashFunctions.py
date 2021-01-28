import hashlib
import random

INT_SIZE = 32
INT_SIZE_BYTES = 4


def generateHashFunctions(n):
    """
    Generates n amount of random hashfunctions, these will be a bunch of random xor values
    :param n: amount of hash functions to create
    :return: a list of n xor values in a tuple object
    the reason for this tuple object is so we can if need be, expand our hash function with other variables
    """
    hashFunction = []
    for i in range(n):
        # Chooses random value to use as xor during a single hash function
        random_XORvalue = random.getrandbits(INT_SIZE)
        hashFunction.append((random_XORvalue))
    return hashFunction


def LSH_hash(value, XORvalue):
    """
    Performs a hash for the LSH algorithm
    :param value: the value of the shingle
    :param XORvalue: the xorvalue unique to this hash value
    :return: the hashed value of "value"
    """
    # Sha1 has is more computational expensive than md5 while for our purpose the specific hash doesnt matter
    #new_value = hashlib.sha1(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_value = hashlib.md5(value.to_bytes(INT_SIZE, 'big')).digest()[0: INT_SIZE_BYTES]
    new_int_value = int.from_bytes(new_value, 'big')
    return new_int_value ^ XORvalue

