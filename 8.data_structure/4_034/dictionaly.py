factorialDic = {}
for i in range(1, 11):
    if i == 1:
        factorialDic[i] =1

    else:
        for j in range(i, (i+1)):
            factorialDic[i] = factorialDic[i -1 ] * j


print(f'factorialDic : {factorialDic}')
