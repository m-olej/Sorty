import random
from sorts import *

# for choosing list size
n = int(input())

# rosnąca lista 

ascendList = []

for l in range(n):
    ascendList.append(l)

# malejąca lista

descendList = []

for i in range(n):
    descendList.append((n-1) - i)

# listy akształtne 
# parzyste rosnące, nieparzyste malejące i viceversa

# unShapedList = []
even = []
uneven = []

for s in range(0 ,n, 2):
    even.append(s)

for t in range(1, n, 2):
    uneven.append(t)
uneven.reverse()    

if len(even) > len(uneven):
    uneven.append(n)
    unShapedList = [sub[item] for item in range(len(uneven)) for sub in [even, uneven]]  
    unShapedList2 = [sub[item] for item in range(len(uneven)) for sub in [uneven, even]]
    unShapedList.remove(n)
    unShapedList2.remove(n)
else:
    unShapedList = [sub[item] for item in range(len(uneven)) for sub in [even, uneven]]  
    unShapedList2 = [sub[item] for item in range(len(uneven)) for sub in [uneven, even]]

# a-kształtne v.2 
unShapedListv2 = even + uneven
# v-kształtne v.2
unShapedListv22 = uneven + even


# random List

randList = []

for y in range(n):
    randList.append(int(random.random()*n))

aList= []
mid = n//2

a1 = randList[:mid]
a2 = randList[mid:]
a1.sort()
a2.sort(reverse=True)

aList = a1 + a2


# Ciągła lista

const = int(random.random()*n)

constList = [const]*n

# print(ascendList)
# print(descendList)
# print(unShapedList)
# print(aList)
# print(randList)
# print(constList)
# print('_________________')

listArray = [ascendList, descendList, unShapedList, aList, randList, constList]

for b in listArray:
    print(b)
    print('_'*n)
    print(selectionSort(b))
    print('-'*n)
