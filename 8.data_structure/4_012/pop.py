playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]

minScoreIdx = 0; minScore = 0
maxScoreIdx = 0; maxScore = 0

for idx, score in enumerate(playerScore):
    if idx == 0 or minScore > score:
        minScore = score
        minScoreIdx = idx

print(f'minScore : {minScore}, minScoreIdx : {minScoreIdx}')
playerScore.pop(minScoreIdx)

# 첫번째 반복문 실행 시
# idx = 0 -> minScoreIdx = 0
# minScore = 9.5
#
# 두번째 반복문 실행 시
# idx = 1 ,minScore = 9.5, score = 8.9
# minScore > score 조건에 의하여
# minScore = score= =8.9
# minScoreIdx = idx = 1
#
# 상기와 같은 순서대로 반복 진행

for idx, score in enumerate(playerScore):
    if maxScore < score:
        maxScore = score
        maxScoreIdx = idx

print(f'maxScore : {maxScore}, maxScoreIdx : {maxScoreIdx}')
playerScore.pop(maxScoreIdx)

print(f'playerScore : {playerScore}')

