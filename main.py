from sorts import *
from GeneratorDanych import *




for n in testSizeList:
    listDict, sedwick_list = generator(n)
    print(f"Testy dla {n} elementów")
    print("-"*n)
    print(f"lista Sedwicka: {sedwick_list}")
    for k in listDict.keys():
        print(f"Unsorted {k}: \n {listDict[k]}")
        print('-'*n)
        currentArray = listDict[k][:]
        for l in sortsDict.keys():
            print(f"Sorted list by {l} \n {sortsDict[l](currentArray)}")



