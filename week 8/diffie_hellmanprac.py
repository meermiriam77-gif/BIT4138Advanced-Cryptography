
print(" Diffie-Hellman Key Exchange ")


p = int(input("Enter the prime number (p): "))
g = int(input("Enter the generator (g): "))


private_A = int(input("Enter User A's private key: "))
private_B = int(input("Enter User B's private key: "))


public_A = pow(g, private_A, p)
public_B = pow(g, private_B, p)

print("\n Public Keys ")
print("User A Public Key:", public_A)
print("User B Public Key:", public_B)


shared_secret_A = pow(public_B, private_A, p)
shared_secret_B = pow(public_A, private_B, p)

print("\n Shared Secret Keys ")
print("User A Shared Secret:", shared_secret_A)
print("User B Shared Secret:", shared_secret_B)


if shared_secret_A == shared_secret_B:
    print("\nKey Exchange Successful!")
    print("Shared Secret Key:", shared_secret_A)
else:
    print("\nKey Exchange Failed!")