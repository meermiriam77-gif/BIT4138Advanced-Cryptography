print(" MINI AES-INSPIRED SPN CIPHER\n")

sbox = {
    "0000":"1110", "0001":"0100", "0010":"1101", "0011":"0001",
    "0100":"0010", "0101":"1111", "0110":"1011", "0111":"1000",
    "1000":"0011", "1001":"1010", "1010":"0110", "1011":"1100",
    "1100":"0101", "1101":"1001", "1110":"0000", "1111":"0111"
}


def key_mix(state, key):
    return ''.join(str(int(a)^int(b)) for a,b in zip(state,key))

def substitute(state):
    return sbox[state]

def permute(state):
    return state[1] + state[3] + state[0] + state[2]

def encrypt(plain, key, rounds):
    state = plain

    print("Initial State:", state)

    for r in range(rounds):
        print(f"\nRound {r+1}")

        state = key_mix(state, key)
        print("After Key Mix:", state)

        state = substitute(state)
        print("After Substitution:", state)

        state = permute(state)
        print("After Permutation:", state)

    return state

plaintext = input("Enter 4-bit plaintext: ")
key = input("Enter 4-bit key: ")
rounds = int(input("Enter number of rounds: "))

cipher = encrypt(plaintext, key, rounds)

print("\nFINAL CIPHERTEXT:", cipher)