import near

scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top5PlayerScores = [9.12, 8.85, 8.12, 7.90, 7.88]
print(f'top5PlayerScores : {top5PlayerScores}')

total = 0; average = 0
for n in scores:
    total += n

average = round(total / len(scores), 2)
print(f'total : {total}')
print(f'average : {average}')

tp = near.Top5Players(top5PlayerScores, average)
tp.setAliScore()
top5PlayerScores = tp.getFinalScores()
print(f'top5PlayerScores : {top5PlayerScores}')