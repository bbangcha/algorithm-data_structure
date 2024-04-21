nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

print(f'nums : {nums}')
print(f'len(nums) : {len(nums)}')

searchData = int(input('input search number : '))
searchResultIdx = -1

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums : {nums}')
print(f'len(nums) : {len(nums)}')
print(f'searchResultIdx : {searchResultIdx}')

if searchResultIdx < 0:
    print('not search index')
else:
    print(f'search index : {searchResultIdx}')
