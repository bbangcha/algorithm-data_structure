import random

types = ['A', 'B', 'O', 'AB']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print(f'todayData : {todayData}')
print(f'todayData length : {len(todayData)}')

for type in types:
    print(f'{type}형 \t : {todayData.count(type)}개')