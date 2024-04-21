students = ['김성예', '신경도', '박기준', '최승철', '황동석']

for i in range(5):
    if i % 2 == 0:
        print(f'인덱스 짝수 : student[{i}] :  {i}')
    else:
        print(f'인덱스 홀수 : student[{i}] :  {i}')