students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print(students)

searchCnt = students.count('강호동')
print(f'강호동의 갯수 : {searchCnt}')

del students[1]
print(students)

del students[0:2]
print(students)



