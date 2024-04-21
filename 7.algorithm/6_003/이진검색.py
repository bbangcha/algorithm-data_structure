datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

searchData = int(input('search data : '))
searchResultIdx = -1

staIdx = 0
endIdx = len(datas) - 1
midIdx = (staIdx + endIdx) // 2
midVal = datas[midIdx]

while searchData <= datas[len(datas) - 1] and searchData >= datas[0]:

    if searchData == datas[len(datas) - 1]:
        searchResultIdx = len(datas) - 1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx : {searchResultIdx}')
