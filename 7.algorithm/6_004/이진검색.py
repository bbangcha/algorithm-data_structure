nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
print(nums)

nums.sort()
print(nums)

searchData = int(input('search data : '))
searchResultIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchData > nums[0] and searchData <= nums[len(nums) - 1]:

    if searchData == nums[len(nums) - 1]:
        searchResultIdx = len(nums) - 1
        break

    elif searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        # print(f'midIdx : {midIdx}')
        # print(f'midVal : {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        # print(f'midIdx : {midIdx}')
        # print(f'midVal : {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break


print(f'searchResultIdx : {searchResultIdx}')


