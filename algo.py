class Alphabet:
    def __init__(self,lower=" ",upper="~"):
        self.lower = ord(lower)
        self.upper = ord(upper)
        self.alphabet = [chr(i) for i in range(self.lower,self.upper+1)]

    # move alphabet to rotor position
    def cycle(self,pos):
        for i in range(pos):
            self.alphabet.append(self.alphabet[0])
            self.alphabet.pop(0)
        return self.alphabet