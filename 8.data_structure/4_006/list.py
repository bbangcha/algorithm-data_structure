korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))
sciScore = int(input('과학 점수 : '))
hisScore = int(input('국사 점수 : '))

minScore = 60

scores = [['국어', korScore], ['영어', engScore], ['수학', matScore],
          ['과학', sciScore], ['국사', hisScore]]

for subject, score in scores:
    if score < minScore:
        print(f'과락과목 : {subject}, 점수 : {score}')