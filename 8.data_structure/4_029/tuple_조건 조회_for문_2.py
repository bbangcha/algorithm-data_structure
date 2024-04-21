students = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

minClassNo = 0; maxClassNo = 0
minClassCnt = 0; maxClassCnt = 0

for classNo, cnt in students:
    if minClassCnt == 0 or minClassCnt > cnt:
        minClassNo = classNo
        minClassCnt = cnt

    if maxClassCnt < cnt:
        maxClassNo = classNo
        maxClassCnt = cnt

print(f'학생수가 가장 적은 학급(학생수) : {minClassNo}학급({minClassCnt}명)')
print(f'학생수가 가장 많은 학급(학생수) : {maxClassNo}학급({maxClassCnt}명)')