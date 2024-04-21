myFavoriteNumber = (1, 3, 5, 6, 7)
friendFavoriteNumber = (2, 3, 5, 8, 10)

print(f'myFavoriteNumber : {myFavoriteNumber}')
print(f'friendFavoriteNumber : {friendFavoriteNumber}')

for n in friendFavoriteNumber:
    if n not in myFavoriteNumber:
        myFavoriteNumber = myFavoriteNumber + (n, )

print(f'myFavoriteNumber : {myFavoriteNumber}')
