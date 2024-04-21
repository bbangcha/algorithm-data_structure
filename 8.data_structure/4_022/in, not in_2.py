import random

randomNumbers = random.sample(range(1,11), 5)
userNumbers = int(input('숫자입력 : '))

print(f'randomNumbers : {randomNumbers}')
print(f'userNumbers : {userNumbers}')

if userNumbers in randomNumbers:
    print('빙고!')
else:
    print('다음 기회에~')

