print(" DIFFERENTIAL CRYPTANALYSIS SIMULATION \n")
sbox = {
    "0000":"1110","0001":"0100","0010":"1101","0011":"0001",
    "0100":"0010","0101":"1111","0110":"1011","0111":"1000",
    "1000":"0011","1001":"1010","1010":"0110","1011":"1100",
    "1100":"0101","1101":"1001","1110":"0000","1111":"0111"
}

def encrypt(p):
    return sbox[p]

p1 = input("Enter plaintext 1 (4-bit): ")
p2 = input("Enter plaintext 2 (4-bit): ")

c1 = encrypt(p1)
c2 = encrypt(p2)

print("\n RESULTS ")
print("Plaintext 1:", p1, "->", c1)
print("Plaintext 2:", p2, "->", c2)

diff_plain = sum(a != b for a, b in zip(p1, p2))
diff_cipher = sum(a != b for a, b in zip(c1, c2))

print("\n DIFFERENCES ")
print("Plaintext difference bits:", diff_plain)
print("Ciphertext difference bits:", diff_cipher)

print("\nObservation:")
print("Small changes in plaintext create unpredictable ciphertext changes.")