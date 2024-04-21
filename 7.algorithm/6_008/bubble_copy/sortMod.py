def bubbleSort(ns):

    length = len(ns) - 1
    for i in range(length):
        for j in range(length -i):
            if ns[j] > ns[j +1]:
                ns[j], ns[j +1] = ns[j +1], ns[j]

    return ns

