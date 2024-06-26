class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
maxAlo = MaxAlgorithm(nums)
maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum()
print(f'maxNum : {maxNum}')


indexes = [0 for i in range((maxNum) + 1)]
print(f'indexes : {indexes}')

for n in nums:
    indexes[n] = indexes[n] + 1
print(f'indexes : {indexes}')

maxAlo = MaxAlgorithm(indexes)
maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum()
maxNumIdx = maxAlo.getMaxNumIdx()
print(f'maxNum : {maxNum}, maxNumIdx : {maxNumIdx}')

print(f'즉, ({maxNumIdx})빈도수가 ({maxNum})로 가장 높다')
