sbox = {
    '0000':'1110',
    '0001':'0100',
    '0010':'1101',
    '0011':'0001',
    '0100':'0010',
    '0101':'1111',
    '0110':'1011',
    '0111':'1000',
    '1000':'0011',
    '1001':'1010',
    '1010':'0110',
    '1011':'1100',
    '1100':'0101',
    '1101':'1001',
    '1110':'0000',
    '1111':'0111'
}

def substitute(bits):
    return sbox[bits]

def permute(bits):
    # Permutation:
    # 1->2, 2->4, 3->1, 4->3
    return bits[2] + bits[0] + bits[3] + bits[1]

plaintext = input("Enter a 4-bit binary number: ")

substituted = substitute(plaintext)
permuted = permute(substituted)

print("After Substitution :", substituted)
print("After Permutation  :", permuted)
print("Ciphertext         :", permuted)