students = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

sum = 0
avg = 0

n = 0

while n < len(students):
    classNo = students[n][0]
    cnt = students[n][1]
    print(f'{classNo}학급 학생 수 : {cnt}')

    sum += cnt
    n += 1

print(f'전체 학생 수 : {sum}')
print(f'평균 학생 수 : {sum / len(students)}')