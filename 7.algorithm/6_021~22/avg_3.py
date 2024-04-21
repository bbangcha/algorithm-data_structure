# 정수와 실수가 섞여 있는 리스트 중 정수들 만의 평균
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
print(f'nums : {nums}')

total = 0
targetNumber = []
for n in nums:
    if n - int(n) == 0: # 정수의 조건
    # if n - int(n) != 0: 실수의 조건
        total += n
        targetNumber.append(n)

average = total / len(targetNumber)
print(f'targetNumber : {targetNumber}')
print(f'average : {round(average, 2)}')


