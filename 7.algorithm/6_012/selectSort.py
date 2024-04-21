import random
import selectMod as sm
import copy #깊은 복사 : copy.deepcopy() 사용

scores = random.sample(range(50, 101), 20)

print(f'scores : {scores}')
result = sm.sortNumber(copy.deepcopy(scores), asc=True) #오름차순
print(f'result : {result}')


print(f'scores : {scores}')
result = sm.sortNumber(copy.deepcopy(scores), asc=False) #내림차순
print(f'result : {result}')
