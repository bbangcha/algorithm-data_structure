import random

sampleList = random.sample(range(1, 11), 10)

selectIdx = int(input('숫자 7의 위치 입력 : '))
searchIdx = sampleList.index(7)

if selectIdx == searchIdx:
    print('빙고!!')

else:
    print('ㅠㅠ')

print(f'sampleList : {sampleList}')
print(f'searchIdx : {searchIdx}')