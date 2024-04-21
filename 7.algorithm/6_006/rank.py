import rankMod as rm
import random

midStdScos = random.sample(range(50, 101), 20)
endStdScos = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(midStdScos, endStdScos)
rd.setMidRank()
print(f'midStuScores : {midStdScos}')
print(f'mid_rank : {rd.getMidRank()}')

rd.setEndRank()
print(f'endStuScores : {endStdScos}')
print(f'end_rank : {rd.getEndRank()}')

rd.printRnakDeviation()


