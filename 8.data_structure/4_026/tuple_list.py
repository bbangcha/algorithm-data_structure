playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)

playerScore = list(playerScore)
playerScore.sort()
print(f'{playerScore} : {playerScore}')
playerScore.pop(0)
playerScore.pop(len(playerScore)-1)
playerScore = tuple(playerScore)
print(f'{playerScore} : {playerScore}')

sum = 0
avg = 0

for i in playerScore:
    sum += i

# print(f'총점 : {round(sum)}')
# print(f'평균 : {round(sum / len(playerScore))}')

avg = sum / len(playerScore)

print('총점 : %.2f' % sum)
print('평균 : %.2f' % avg)