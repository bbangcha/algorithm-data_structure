studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

sum = 0
avg = 0

for classNo, cnt in studentCnts:
    print(f'{classNo}학급의 학생수  : {cnt}')
    sum += cnt

print(f'전체 학생 수 : {sum}')
print(f'평균 학생 수 : {sum / len(studentCnts)}')