import random
import sortMod as sm

nums = random.sample(range(1, 1000), 100)
print(f'not sorted numbers : {nums}')

# 객체생성
sn = sm.SortNumber(nums)

# 오름차순(ascending)
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers by ASC : {sortedNumbers}')

# 내림차순(descending)
sn.isAscending(False)
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers by DESC : {sortedNumbers}')

# min & max
print(f'getMinNumber : {sn.getMinNumber()}')
print(f'getMaxNumber : {sn.getMaxNumber()}')


