scores = {'kor' : 88, 'eng' : 55, 'mat' : 85, 'sci' : 57, 'his' : 82}

print(f'scores ; {scores}')

minScore = 60
fStr = 'F(재시험)'

if scores['kor'] < minScore : scores['kor'] = fStr
if scores['eng'] < minScore : scores['eng'] = fStr
if scores['mat'] < minScore : scores['mat'] = fStr
if scores['sci'] < minScore : scores['sci'] = fStr
if scores['his'] < minScore : scores['his'] = fStr

print(f'scores ; {scores}')
