students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']

print(students)

searchIdx = students.index('강호동')

print(f'searchIdx : {searchIdx}')

# 반복되는 단어의 경우 범위지정이 없을 시 맨처음 인덱스 값만 추출

searchIdx = students.index('강호동', 2, 6)

print(f'searchIdx : {searchIdx}')

# 반복되는 단어의 경우 범위지정이 있을 시 지정된 범위 내의 인덱스 값만 추출
