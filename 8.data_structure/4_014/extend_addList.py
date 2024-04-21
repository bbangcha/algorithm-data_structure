myFavoriteNumber = [1, 3, 5, 6, 7]
friendFavoriteNumber = [2, 3, 5, 8, 10]

addList = myFavoriteNumber + friendFavoriteNumber

print(f'addList : {addList}')

result = []
for number in addList:
    if number not in result:
        result.append(number)

print(f'result : {result}')