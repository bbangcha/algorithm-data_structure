class Top5Players:

    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScores = ns

    def setAliScore(self):

        nearIdx = 0
        nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScores - s)

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        if self.newScores >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores)-1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i - 1]

            self.currentScores[nearIdx] = self.newScores

        else:
            for i in range(len(self.currentScores) - 1, nearIdx+ 1, -1):
                self.currentScores[i] = self.currentScores[i - 1]

            self.currentScores[nearIdx] = self.newScores

    def getFinalScores(self):
        return self.currentScores