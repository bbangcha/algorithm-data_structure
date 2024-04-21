myInfo = {'이름' : 'Hong gil dong',
          '나이' : '30',
          '연락처' : '010-1234-5678',
          '주민등록번호' : '840315-1234567',
          '주소' : '대한민국 서울'}

print(f'myInfo : {myInfo}')

deleteItems = ['연락처', '주민등록번호']

for item in deleteItems:
    if item in myInfo:
        del myInfo[item]

print(f'myInfo : {myInfo}')
