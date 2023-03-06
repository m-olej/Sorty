from sorts import *
from GeneratorDanych import *
from timeit import timeit 
# for choosing list size
# n = int(input())

for n in testSizeList:
    print(n)
    print("-"*n)
    listDict, sedwick_list = generator(n)
    listNameArray = list(listDict.keys())
    listArray = listDict.values()
    sortsList = list(sortsDict.keys())
    # print(sedwick_list)
    for k, v in listDict.items():
        print(f"Unsorted {k}: \n {v}")
        print('-'*n)
        for l, b in sortsDict.items():
            print(f"Sorted list by {l} \n {b(v)}")



