students = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

sum = 0
avg = 0

for classNo, student in students:
    print(f'{classNo}반의 학생수  : {student}')
    sum += student

print(f'전체 학생 수 : {sum}')
print(f'평균 학생 수 : {sum / len(students)}')