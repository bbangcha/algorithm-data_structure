students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

slength = len(students)

for i in range(len(students)):
    print(students[i])

print('-' * 20)

# range로 범위를 정하지 않고{range(len(students))} 바로 반복횟수를 정할 수 있다{students}
for j in students:
    print(j)