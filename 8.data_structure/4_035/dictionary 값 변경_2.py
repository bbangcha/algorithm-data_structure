myBodyInfo = {'이름':'gil dong', '몸무계':83, '신장':1.8}
myBMI = myBodyInfo['몸무계'] / (myBodyInfo['신장'] ** 2)
print(f'myBodyInfo : {myBodyInfo}')
print(f'myBMI : {myBMI}')

date = 0

while True:
    date += 1

    myBodyInfo['몸무계'] = round((myBodyInfo['몸무계'] - 0.3), 2)
    print('몸무계 : {}'.format(myBodyInfo['몸무계']))

    myBodyInfo['신장'] = round((myBodyInfo['신장'] + 0.001), 3)
    print('몸무계 : {}'.format(myBodyInfo['신장']))

    myBMI = myBodyInfo['몸무계'] / (myBodyInfo['신장'] ** 2)

    if date >= 30:
        break

print(myBodyInfo)
print(round(myBMI), 2)
