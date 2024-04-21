nums = [10, 2, 7, 21, 0]
print(f'not sorted nums : {nums}')

lenth = len(nums) - 1
for i in range(lenth):
    for j in range(lenth - i):
        if nums[j] > nums[j + 1]:
            # a,b 자리 바꾸는 공식 : a, b = b, a
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

        print(nums)
    print()

print(f'sorted nums : {nums}')