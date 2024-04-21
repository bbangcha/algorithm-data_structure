students = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

minClassNo = 0; maxClassNo = 0
minCnt = 0; maxCnt = 0

sum = 0
avg = 0

n = 0
while n < len(students):
    if minCnt == 0 or minCnt > students[n][1]:
        minClassNo = students[n][0]
        minCnt = students[n][1]

    if maxCnt < students[n][1]:
        maxClassNo = students[n][0]
        maxCnt = students[n][1]

    sum += students[n][1]
    n += 1

print(f'학생수가 가장 적은 학급(학생수) : {minClassNo}학급({minCnt}명)')
print(f'학생수가 가장 많은 학급(학생수) : {maxClassNo}학급({maxCnt}명)')