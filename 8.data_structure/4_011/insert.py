numbers = [1, 3, 6, 11, 45, 62, 74, 85]

inputNumber = int(input('숫자 입력 : '))

insertIdx = 0

for idx, number in enumerate(numbers):
    print(idx, number)

    if insertIdx == 0 and inputNumber < number:
        insertIdx = idx

numbers.insert(insertIdx, inputNumber)
print(numbers)