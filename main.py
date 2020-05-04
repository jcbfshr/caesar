import cipher
shift = int(input("Shift: "))

for char in str(input("Plaintext: ")):
    print(cipher.encrypt(char,shift),end="")
print()

print(f"Use key {shift*-1} to decrypt")