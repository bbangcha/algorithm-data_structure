import random as rd
import sortMod as sm

rNums = rd.sample(range(1, 101), 10)
print(f'not sorted rNums : {rNums}')
print(f'sorted rNums  ASC : {sm.qSort(rNums, asc = True)}')
print(f'sorted rNums  DESC : {sm.qSort(rNums, asc = False)}')
