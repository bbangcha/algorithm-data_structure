studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

for i in range(len(studentCnts)):
    print(f'{studentCnts[i][0]}학급의 학생 수 : {studentCnts[i][1]}')

print('- * 20')

for classNo, cnt in studentCnts:
    print(f'{classNo}학급의 학생 수 : {cnt}')