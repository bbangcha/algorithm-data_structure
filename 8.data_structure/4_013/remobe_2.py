myList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']

removeList = input('삭제 대상 입력 : ')
myList.remove(removeList)
print(f'일정 : {myList}')

subject = ['국어', '영어', '수학', '과학', '국사', '국어', '영어', '수학', '과학', '국사']

removeSubject = input('삭제 과목 입력 : ')
while removeSubject in subject:
    subject.remove(removeSubject)

print(f'시험 과목표 : {subject}')
