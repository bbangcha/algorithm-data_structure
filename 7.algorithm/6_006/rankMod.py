class RankDeviation:

    def __init__(self, mss, ess):
        self.midStdScos = mss
        self.endStdScos = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(ess))]
        self.rankDeviation = [0 for i in range(len(ess))]

    def setRank(self, ss, rs):
        for idx, score1 in enumerate(ss):
            for score2 in ss:
                if score1 < score2:
                    rs[idx] += 1

    def setMidRank(self):
        self.setRank(self.midStdScos, self.midRanks)

    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endStdScos, self.endRanks)

    def getEndRank(self):
        return self.endRanks

    def printRnakDeviation(self):

        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]

            if deviation > 0:
                deviation = '↑' + str(abs(deviation))

            elif deviation < 0:
                deviation = '↓' + str(abs(deviation))

            else:
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank : {mRank} \t end_rank : {self.endRanks[idx]} \t Deviation : {deviation}')


