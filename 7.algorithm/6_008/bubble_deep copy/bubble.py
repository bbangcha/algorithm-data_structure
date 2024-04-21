import random as rd
import sortMod as sm

students = []

for i in range(20):
    students.append(rd.randint(170, 185))

print(f'students : {students}')

sortedStudents = sm.bubbleSort(students, deepcopy=True) #deepcopy=True 생략 가능

print(f'students : {students}') # 깊은 복사로 기존의 데이터는 그대로 유지
print(f'sortedStudents : {sortedStudents}')
