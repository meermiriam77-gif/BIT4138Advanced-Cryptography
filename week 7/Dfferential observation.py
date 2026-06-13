print("DIFFERENTIAL OBSERVATION \n")


sbox = {
    "0000":"1110","0001":"0100","0010":"1101","0011":"0001",
    "0100":"0010","0101":"1111","0110":"1011","0111":"1000",
    "1000":"0011","1001":"1010","1010":"0110","1011":"1100",
    "1100":"0101","1101":"1001","1110":"0000","1111":"0111"
}

def encrypt(msg):
    return sbox[msg]

m1 = "0011"
m2 = "0010"

c1 = encrypt(m1)
c2 = encrypt(m2)

print("Message 1:", m1, "-> Cipher:", c1)
print("Message 2:", m2, "-> Cipher:", c2)

diff = sum(a != b for a, b in zip(c1, c2))

print("\nBit differences in ciphertext:", diff)