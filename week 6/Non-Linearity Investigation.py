

print(" NON-LINEARITY EXPERIMENT \n")

sbox = {
    "0000": "1110",
    "0001": "0100",
    "0010": "1101",
    "0011": "0001",
    "0100": "0010",
    "0101": "1111",
    "0110": "1011",
    "0111": "1000",
    "1000": "0011",
    "1001": "1010",
    "1010": "0110",
    "1011": "1100",
    "1100": "0101",
    "1101": "1001",
    "1110": "0000",
    "1111": "0111"
}


plain = input("Enter a 4-bit binary number (e.g. 0001): ")


cipher = sbox.get(plain, "Invalid input")

print("\n RESULT")
print("Input Plaintext :", plain)
print("After S-Box     :", cipher)

def flip_first_bit(bits):
    return ('1' if bits[0] == '0' else '0') + bits[1:]

near_input = flip_first_bit(plain)

near_output = sbox.get(near_input, "Invalid")

print("\n NON-LINEARITY CHECK ")
print("Near Input      :", near_input)
print("Near Output     :", near_output)

print("\n OBSERVATION ")
print("Small change in input gives a very different output.")
print("This shows NON-LINEARITY in the S-Box.")