from sorts import *
from GeneratorDanych import *
from timeit import Timer

for n in testSizeList:
    print(f"Testy dla {n} elementów")
    print("-"*n)
    for a, s in sortsDict.items():
        listDict, sedwick_list = generator(n)
        for k, v in listDict.items():
            print(f"Unsorted {k}: {v}")
            print(f"Sorted by {a} \n {s(v)}")
            t = Timer(lambda: s(v))
            print(f"Time taken by algorithm: {t.timeit()} s")
            

