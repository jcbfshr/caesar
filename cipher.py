import algo
charset = algo.Alphabet()

# encrypt plaintext by shift value
def encrypt(letter,shift):
    # convert letter to integer, add shift modulo length of alphabet (wrap-around), convert back to letter
    return charset.alphabet[(charset.alphabet.index(letter)+shift)%len(charset.alphabet)]