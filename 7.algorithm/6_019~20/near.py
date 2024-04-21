import random

nums = random.sample(range(0, 50), 20)
print(f'nums : {nums}')

inputNum = int(input('input number : '))
print(f'inputNum : {inputNum}')

nearNum = 0
minNum = 50 #데이터가 많을 시 maxAlgorithm으로 최대값을 최소값으로 설정

for n in nums:
    absNum = abs(n - inputNum)
    # print(f'absNum : {absNum}')

    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum : {nearNum}')


