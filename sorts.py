from GeneratorDanych import sedgewick
import sys
import random
sys.setrecursionlimit(10000)
def selectionSort(array):
  n = len(array)
  new_array = []
  while n > 0:
    minVal = min(array)
    minIndex = array.index(minVal)
    new_array.append(minVal)
    array.pop(minIndex)
    n -= 1
  return new_array


def insertionSort(array):
  new_array = []
  for j in range(1, len(array)):
    while j > 0 and array[j] < array[j-1]:
       temp = array[j-1]
       array[j-1] = array[j]
       array[j] = temp
       j -= 1
    new_array = array[:]
    return new_array


def shellSort(array):
    new_array = list(array)
    global sedgewick
    for val in sedgewick:
        for i in range(val, len(new_array)):
            temp = new_array[i]
            j = i
            while j >= val and new_array[j - val] > temp:
                new_array[j] = new_array[j - val]
                j -= val
            new_array[j] = temp
    return new_array


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

    #---------------ROBIENIE KOPCA----------------
    for i in range(len(array)//2 - 1, -1, -1):
        kopcowanie(array, len(array), i)

    # #-------------Root z kopca idzicie na koniec---------
    for i in range(len(array)-1, 0, -1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        kopcowanie(array, i, 0)

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

test = [5, 6, 7, 8, 1, 2, 9]
quickSortRandom(test, 0, len(test) - 1)



sortsDict = {
    "selection sort": selectionSort,
    "insertion sort": insertionSort,
    "sedgewick shell sort": shellSort,
    "heap sort": heapSort
}