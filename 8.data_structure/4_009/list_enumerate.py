sports = ['농구', '수구', '축구', '마라톤', '테니스']

favoriteSport = input('가장 좋아하는 스포츠 입력 : ')
bestSportIdx = 0

for index, value in enumerate(sports):
    if value == favoriteSport:
        bestSportIdx = index +1

print(f'{favoriteSport}(은)는 {bestSportIdx}번째에 있습니다.')
