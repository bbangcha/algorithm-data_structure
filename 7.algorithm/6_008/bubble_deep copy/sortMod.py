import copy

def bubbleSort(ns, deepcopy = True):

    if deepcopy:
        cns = copy.copy(ns)
    else:
        cns = ns

    length = len(cns) - 1
    for i in range(length):
        for j in range(length -i):
            if cns[j] > cns[j +1]:
                cns[j], cns[j +1] = cns[j +1], cns[j]

    return cns

