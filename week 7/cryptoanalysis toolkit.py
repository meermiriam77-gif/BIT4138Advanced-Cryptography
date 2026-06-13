import collections

print(" MINI CRYPTANALYSIS TOOLKIT \n")

sbox = {
    "0000":"1110","0001":"0100","0010":"1101","0011":"0001",
    "0100":"0010","0101":"1111","0110":"1011","0111":"1000",
    "1000":"0011","1001":"1010","1010":"0110","1011":"1100",
    "1100":"0101","1101":"1001","1110":"0000","1111":"0111"
}

def encrypt(p):
    return sbox.get(p, "????")

def difference(p1, p2):
    return sum(a != b for a, b in zip(p1, p2))

def frequency(ciphertexts):
    freq = collections.Counter(ciphertexts)
    print("\n FREQUENCY ANALYSIS ")
    for k, v in freq.items():
        print(k, ":", v)

def bias(ciphertexts):
    freq = collections.Counter(ciphertexts)
    total = len(ciphertexts)
    print("\n STATISTICAL BIAS ")
    for k, v in freq.items():
        print(f"{k} bias = {v/total:.2f}")

print("Enter two plaintexts (4-bit each):")
p1 = input("Plaintext 1: ")
p2 = input("Plaintext 2: ")

c1 = encrypt(p1)
c2 = encrypt(p2)

print("\n ENCRYPTION RESULTS ")
print(p1, "->", c1)
print(p2, "->", c2)

diff = difference(p1, p2)
print("\n DIFFERENCE ANALYSIS ")
print("Bit difference:", diff)

dataset = [encrypt(p1), encrypt(p2),
           encrypt("0001"), encrypt("0010"),
           encrypt("0011"), encrypt("0100")]

frequency(dataset)

bias(dataset)

print("\n AVALANCHE EFFECT ")

flip = '1' + p1[1:] if p1[0] == '0' else '0' + p1[1:]
c_flip = encrypt(flip)

print("Original :", p1, "->", c1)
print("Flipped  :", flip, "->", c_flip)

avalanche = sum(a != b for a, b in zip(c1, c_flip))
print("Avalanche difference:", avalanche, "/4")

print("\n END OF ANALYSIS ")