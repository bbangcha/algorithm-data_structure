# 난수 중 50이상 90 이하 수들의 평균
import random

nums = random.sample(range(0, 100), 30)
print(f'nums : {nums}')

total = 0
targetNumber = []
for n in nums:
    if n >= 50 and n <= 90: # 난수 중 50이상 90 이하 수 조건
        total += n
        targetNumber.append(n)

average = total / len(targetNumber)
print(f'targetNumber : {targetNumber}')
print(f'average : {round(average, 2)}')


