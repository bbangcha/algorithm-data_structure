def qSort(ns, asc=True):

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

    if asc:
        return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)
    else:
        return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)
    # 재귀함수 호출 시 입력 값이 False라도 기본값인 True가 적용되므로
    # "asc = asc"를 통해서 명시해준 후 입력 값과 동일하게 재귀함수도 입력되도록 해야된다
