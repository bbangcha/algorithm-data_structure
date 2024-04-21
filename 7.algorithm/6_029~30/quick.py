def qSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midValue = ns[midIdx]

    smallNums = []; sameNums = []; bigNums = []
    for n in ns:
        if n < midValue:
            smallNums.append(n)
        elif n == midValue:
            sameNums.append(n)
        elif n > midValue:
            bigNums.append(n)

    return qSort(smallNums) + sameNums + qSort(bigNums)

nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
qSort(nums)
print(f'qSort(nums) : {qSort(nums)}')
