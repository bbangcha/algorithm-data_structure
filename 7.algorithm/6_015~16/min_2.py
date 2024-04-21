class MinAlgorithm:

    def __init__(self, cs):
        self.chars = cs
        self.minChar = 0

    def getMinChar(self):

        self.minChar = self.chars[0]

        for c in self.chars:
            if ord(self.minChar) > ord(c):
                self.minChar = c

        return self.minChar


chars = ['c','x', 'Q', 'A', 'e', 'P', 'p']
cm = MinAlgorithm(chars)
minChar = cm.getMinChar()
print(f'minChar : {minChar}')

