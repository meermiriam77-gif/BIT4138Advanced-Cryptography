print(" ADVANCED SPN SIMULATOR \n")

sbox = {
    "0000":"1110", "0001":"0100", "0010":"1101", "0011":"0001",
    "0100":"0010", "0101":"1111", "0110":"1011", "0111":"1000",
    "1000":"0011", "1001":"1010", "1010":"0110", "1011":"1100",
    "1100":"0101", "1101":"1001", "1110":"0000", "1111":"0111"
}

def permute(bits):
    return bits[2] + bits[0] + bits[3] + bits[1]


def xor(a, b):
    return ''.join(str(int(x)^int(y)) for x,y in zip(a,b))


def substitute(block):
    return sbox[block]

def round_function(state, key):
    state = xor(state, key)
    state = substitute(state)
    state = permute(state)
    return state

plaintext = input("Enter 4-bit plaintext: ")
key = input("Enter 4-bit key: ")
rounds = int(input("Enter number of rounds: "))

print("\n ENCRYPTION PROCESS ")

state = plaintext

for i in range(rounds):
    state = round_function(state, key)
    print(f"After Round {i+1}: {state}")

ciphertext = state

print("\nCiphertext:", ciphertext)


print("\n AVALANCHE EFFECT TEST ")

flipped = '1' + plaintext[1:] if plaintext[0]=='0' else '0' + plaintext[1:]

state2 = flipped

for i in range(rounds):
    state2 = round_function(state2, key)

print("Original Ciphertext :", ciphertext)
print("Flipped Input Cipher:", state2)


diff = sum(a!=b for a,b in zip(ciphertext, state2))

print("Bit differences:", diff, "/4")