import random
import string
import numpy as np
import itertools
import sys

 
k = 10 #size of the key

key = ""

# Loop to find the string
# of desired length
for i in range(k):
  temp = str(random.randint(0, 1))
  key += temp

# Driver Code

print("Random binary string is: ", key)


L0 = key[:len(key)//2]
R0 = key[len(key)//2:]
# print(L0)
# print(R0)

#PRNF to generate a pseudorandom strings

SEED_SIZE  = 10
GENERATOR  = 2
MODULUS    = 36389



def function_H(first_half, second_half):
    mod_exp = bin(pow(GENERATOR, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit & int(second_half[i])) % 2
    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed):
    binary_string = str(initial_seed)
    result = ''
    for i in range(len(initial_seed)):
        first_half = binary_string[:len(binary_string)//2]
        second_half = binary_string[len(binary_string)//2:]
        binary_string = function_H(first_half, second_half)
        result += binary_string[-1]
        binary_string = binary_string[:-1]
    return result

# xor two strings
def xor(s1, s2):
  return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def fnIsBin(string):
  for character in string:
    if character != '0' and character != '1':
      return False
  return True

# enc function defines the encryption using feistel network for strings containing only 0 and 1.

def enc(key):
  ROUNDS = 3

  ciphertext = ""
  key_initial = key
  L = [""] * (ROUNDS + 1)
  R = [""] * (ROUNDS + 1)
  L[0] = key[:len(key)//2]
  R[0] = key[len(key)//2:]
  # print("L[0] = {}".format(L[0]))
  # print("R[0] = {}".format(R[0]))

  for i in range(1, ROUNDS+1):
    L[i] = R[i - 1]
    l1 =  "".join(str(ord(char)) for char in L[i])
    # if(fnIsBin(l1) == True):
    #   print("L[{}] = {}".format(i, l1))
    # else:
    #   print("L[{}] = {}".format(i, "".join(str(chr(ord(char))) for char in L[i])))
    
    l = str(R[i-1])
    if(fnIsBin(l) == True):
      r = function_G(l)
    else:
      x = "".join(str(ord(char)) for char in l)
      r = function_G(x)
    
    r1 = "".join(str(ord(char)) for char in r)
    # if(fnIsBin(r1) == True):
    #   print("R[{}] = {}".format(i, r1))
    # else:
    #   print("R[{}] = {}".format(i, "".join(str(chr(ord(char))) for char in r)))
    
    R[i] = xor(L[i - 1], r)
    t = "".join(str(ord(char)) for char in R[i])
    R[i] = t

  ciphertext += (L[ROUNDS] + R[ROUNDS])
  return ciphertext

print("key = ", key)
print("enc1 =", enc(key))
print("enc2 =", enc(enc(key)))
