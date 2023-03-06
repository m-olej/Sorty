from sorts import *
from GeneratorDanych import *
# for choosing list size
n = int(input())


listArray, sedwick_list = generator(n)


print(sedwick_list)
for b in listArray:
    print(b)
    print('_'*n)
    heapSort(b)
    print(b)
    print('-'*n)
