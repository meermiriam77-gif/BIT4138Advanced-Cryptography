print(" SPN vs FEISTEL PRACTICAL \n")

sbox = {
    "0000": "1110",
    "0001": "0100",
    "0010": "1101",
    "0011": "0001"
}

plaintext = "0010"

spn_step1 = sbox[plaintext]

print(" SPN ")
print("Plaintext  :", plaintext)
print("After S-Box:", spn_step1)

print("\n FEISTEL (1 ROUND)")

left = "10"
right = "01"

def F(r):
    
    return str(int(r[0]) ^ 1) + str(int(r[1]) ^ 1)

f_result = F(right)

new_left = right
new_right = str(int(left[0]) ^ int(f_result[0])) + str(int(left[1]) ^ int(f_result[1]))

print("Left        :", left)
print("Right       :", right)
print("F(Right)    :", f_result)
print("New Left    :", new_left)
print("New Right   :", new_right)




print("\n COMPARISON ")

print("SPN:")
print("- Uses substitution (S-Box)")
print("- Works on whole block")
print("- Strong confusion + diffusion")

print("\nFeistel:")
print("- Splits block into halves")
print("- Uses round function + XOR")
print("- Same structure for encryption/decryption")

print("\nFINAL CONCLUSION:")
print("SPN is more modern (AES style).")
print("Feistel is simpler but still secure (DES style).")