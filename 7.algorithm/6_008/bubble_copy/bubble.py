import random as rd
import sortMod as sm

students = []

for i in range(20):
    students.append(rd.randint(170, 185))

print(f'students : {students}')

sortedStudents = sm.bubbleSort(students)

print(f'students : {students}') # 얕은 복사로 sortMod 모듈에 의해 기존 데이터도 변형
print(f'sortedStudents : {sortedStudents}')
