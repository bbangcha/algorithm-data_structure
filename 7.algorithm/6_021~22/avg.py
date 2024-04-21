import random

nums = random.sample(range(0, 100), 10)
print(f'nums : {nums}')

total = 0
for n in nums:
    total += n

average = total / len(nums)
print(f'average : {average}')


