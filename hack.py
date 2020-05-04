import cipher,algo
ciphertext = str(input("Ciphertext: "))

charset = algo.Alphabet()

for i in range(len(charset.alphabet)):
    print(f"Key: {i}: ",end="")
    for char in ciphertext:
        print(cipher.encrypt(char,i),end="")
    print()