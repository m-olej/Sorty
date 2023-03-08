from GeneratorDanych import sedgewickList
import sys
import random
sys.setrecursionlimit(10000)
def selectionSort(array):
    for i in range(len(array)):
        minVal = array[i]
        for j in range(i, len(array)):
            if minVal > array[j]:
                minVal = array[j]
                minIndex = j
        if minVal != array[i]:
            temp = array[i]
            array[i] = minVal
            array[minIndex] = temp
    return array


def insertionSort(array):
    new_array2 = array[:]
    for i in range(1, len(new_array2)):
        while i > 0 and new_array2[i] < new_array2[i-1]:
            temp = new_array2[i-1]
            new_array2[i-1] = new_array2[i]
            new_array2[i] = temp
            i -= 1
    return new_array2



def shellSort(array):
    new_array3 = list(array)
    for val in sedgewickList:
        for i in range(val, len(new_array3)):
            temp = new_array3[i]
            j = i
            while j >= val and new_array3[j - val] > temp:
                new_array3[j] = new_array3[j - val]
                j -= val
            new_array3[j] = temp
    return new_array3


def kopcowanie(array, koniec, i):
    rodzic = i
    lewe_dziecko = 2*rodzic + 1
    prawe_dziecko = 2*rodzic + 2
    is_changed = False
    zmiana = None
    #----- Kopcuje się od lewej ------
    if lewe_dziecko < koniec  and array[rodzic] < array[lewe_dziecko]:
        is_changed = True
        zmiana = lewe_dziecko
    if prawe_dziecko < koniec and array[rodzic] < array[prawe_dziecko] and array[prawe_dziecko] > array[lewe_dziecko]:
        is_changed = True
        zmiana = prawe_dziecko
    if is_changed:
        temp = array[rodzic]
        array[rodzic] = array[zmiana]
        array[zmiana] = temp
        #--------- Żeby zmieniło też gałąź pod jesli jest ich więcej----------
        kopcowanie(array, koniec, zmiana)


def heapSort(array):
    new_array4 = array[:]
    #---------------ROBIENIE KOPCA----------------
    for i in range(len(new_array4)//2 - 1, -1, -1):
        kopcowanie(new_array4, len(new_array4), i)

    # #-------------Root z kopca idzicie na koniec---------
    for i in range(len(new_array4)-1, 0, -1):
        temp = new_array4[i]
        new_array4[i] = new_array4[0]
        new_array4[0] = temp
        kopcowanie(new_array4, i, 0)
    return new_array4

#--------------------Qucik Sort--------------------------
def parttioton(array, low, high):
    pivot = array[high]
    start = low
    end = high
    while True:
        while array[start] < pivot:
            start+=1
        while array[end] > pivot:
            end-=1
        if start < end:
            array[start], array[end] = array[end], array[start]
            end-=1
            start+=1
        elif start == end:
            return end - 1
        else:
            return end

def quickSort(array, low, high):
    print(test)
    if low < high:
        pivot = parttioton(array, low, high)
        quickSort(array, low, pivot)
        quickSort(array, pivot + 1, high)


def parttiotonRandom(array, low, high):
    pivot = random.choice(array)
    start = low
    end = high
    while True:
        while array[start] < pivot:
            start+=1
        while array[end] > pivot:
            end-=1
        if start < end:
            array[start], array[end] = array[end], array[start]
            end-=1
            start+=1
        elif start == end:
            return end - 1
        else:
            return end

def quickSortRandom(array, low, high):
    print(test)
    if low < high:
        pivot = parttioton(array, low, high)
        quickSort(array, low, pivot)
        quickSort(array, pivot + 1, high)

# test = [5, 6, 7, 8, 1, 2, 9]
# quickSortRandom(test, 0, len(test) - 1)



sortsDict = {
    "selection sort": selectionSort,
    "insertion sort": insertionSort,
    "Sedgewick shell sort": shellSort,
    "heap sort": heapSort
}


