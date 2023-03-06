import random


# --- list of different amount of arguments to test --- #
# dane o wiele zmniejszone do testów xd #
# testSizeList = [10*x for x in range(1, 3)]
testSizeList = [10]

def generator(n):
    ascendList = list()
    descendList = list()
    aList = list()
    randList = list()
    constList = list()

    #-----------Rosnąca-----------------
    for l in range(n):
        ascendList.append(int(random.random()*n))
    ascendList.sort()    

    # -----------Malejąca-----------------
    for i in range(n):
        descendList.append(int(random.random()*n))
    descendList.sort(reverse=True)    

    # -----------Losowa-----------------
    for s in range(n):
        randList.append(int(random.random() * n))

    # -----------W kształcie A-----------------
    mid = n // 2
    a1 = randList[:mid]
    a2 = randList[mid:]
    a1.sort()
    a2.sort(reverse=True)
    aList = a1 + a2

    # -----------Stała-----------------
    const = int(random.random() * n)
    constList = [const] * n

    # -----------Dane do shellSorta-----------------
    sedwick_list = [1]
    sedwick = 0
    k = 0
    while n >= sedwick:
        sedwick = 4 ** (k + 1) + 3 * 2 ** (k) + 1
        if n > sedwick:
            sedwick_list.append(sedwick)
        k += 1
    sedwick_list.sort(reverse=True)


    return {"ascendList": ascendList, "descendList": descendList, "randList": randList, "aList": aList, "constList": constList}, sedwick_list 

listDict, sedgewick = generator(10)
