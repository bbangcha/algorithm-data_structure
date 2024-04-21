def mSort(ns, asc=True):
    #분할단계
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc = asc)
    rightNums =mSort(ns[midIdx:len(ns)], asc = asc)
    # 재귀함수 호출 시 입력 값이 False라도 기본값인 True가 적용되므로
    # "asc = asc"를 통해서 명시해준 후 입력 값과 동일하게 재귀함수도 입력되도록 해야된다

    #병합단계
    mergeNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]

    return mergeNums