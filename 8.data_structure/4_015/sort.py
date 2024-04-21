playerScore = [9.5, 8.9, 9.2 ,9.8, 8.8, 9.0]

playerScore.sort(reverse=False)
print(f'playerScore : {playerScore}')

playerScore.pop(0)
playerScore.pop(len(playerScore)-1)

print(f'playerScore : {playerScore}')

sum = 0
avg = 0

for score in playerScore:
    sum += score

avg = sum / len(playerScore)

print('점수 합계 : %.2f' % sum)
print(f'점수 합계 : {round(sum, 2)}')

print(f'점수 평균 : {round(sum / len(playerScore), 2)}')
print('점수 평균 : %.2f' % avg)
