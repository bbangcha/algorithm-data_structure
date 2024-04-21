# ascending
nums = [5, 10, 2, 1, 0]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] > cNum and i2 >= 0: # 오름차순 (nums[i2] > cNum)
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2 + 1] = cNum
    print(f'nums : {nums}')

print(f'nums : {nums}')

print('-' * 25)

# descending
nums = [0, 5, 2, 10, 1]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] < cNum and i2 >= 0: # 내림차순 nums[i2] < cNum
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2 + 1] = cNum
    print(f'nums : {nums}')

print(f'nums : {nums}')