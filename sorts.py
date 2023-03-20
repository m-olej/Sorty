import sys
import random
sys.setrecursionlimit(2147483647)
def selectionSort(array):
    for i in range(len(array)):
        minVal = array[i]
        minIndex = i
        for j in range(i, len(array)):
            if minVal > array[j]:
                minVal = array[j]
                minIndex = j
        if array[minIndex] != array[i]:
            array[i], array[minIndex] = minVal, array[i]
    return array


def insertionSort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            temp = array[i-1]
            array[i-1] = array[i]
            array[i] = temp
            i -= 1
    return array
#------------------------------SHELL SORT-----------------------
def sedwick(n):
    sedwick_list = [1]
    sedwick = 0
    k = 0
    while n >= sedwick:
        sedwick = 4 ** (k + 1) + 3 * 2 ** (k) + 1
        if n > sedwick:
            sedwick_list.append(sedwick)
        k += 1
    sedwick_list.sort(reverse=True)
    return sedwick_list


def shellSort(array):
    sedwick_list = sedwick(len(array))
    for val in sedwick_list:
        for i in range(val, len(array)):
            temp = array[i]
            j = i
            while j >= val and array[j - val] > temp:
                array[j] = array[j - val]
                j -= val
            array[j] = temp
    return array

#----------------------------HEAP SORT----------------------------------------

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
    return array

#--------------------Qucik Sort--------------------------

def parttioton(array, low, high):
    pivot = array[high]
    start = low
    end = high
    while True:

        while start < high + 1 and array[start] < pivot:
            start+=1
        while end>-1 and array[end] > pivot:
            end-=1
        if start <= end:
            array[start], array[end] = array[end], array[start]
            end-=1
            start+=1
        else:
            return end

def quickSort(array, low, high):

    if low<high:
        pivot = parttioton(array, low, high)
        quickSort(array, low, pivot)
        quickSort(array, pivot + 1, high)

def parttiotonRan(array, low, high):
    pivot = array[random.randint(low, high)]
    start = low
    end = high
    while True:

        while start < high + 1 and array[start] < pivot:
            start+=1
        while end>-1 and array[end] > pivot:
            end-=1
        if start <= end:
            array[start], array[end] = array[end], array[start]
            end-=1
            start+=1
        else:
            return end

def quickSortRan(array, low, high):

    if low<high:
        pivot = parttiotonRan(array, low, high)
        quickSortRan(array, low, pivot)
        quickSortRan(array, pivot + 1, high)

# test = [5, 6, 7, 8, 1, 2, 9]
# quickSortRandom(test, 0, len(test) - 1)

# def Quicksort(array):
#
#   if len(array) <= 1:
#         return array
#
#   stack = [(0, len(array)-1)]
#
#   while stack:
#
#       left, right = stack.pop()
#       cut = partition(array, left, right)
#       if cut > left:
#           stack.append((left, cut))
#       if cut + 1 < right:
#           stack.append((cut +1, right))
#
#   return array
#
#
# def partition(arr, left, right):
#     pivot = arr[random.randint(left, right)]
#     i = left
#     j = right
#
#     while True:
#       while arr[i] < pivot:
#           i += 1
#       while arr[j] > pivot:
#           j -= 1
#       if i < j:
#           arr[i], arr[j] = arr[j], arr[i]
#           i += 1
#           j -= 1
#       else:
#             return j



sortsDict = {
    # "selection sort": selectionSort,
    # "insertion sort": insertionSort,
    "quick sort": quickSort,
    "Sedgewick shell sort": shellSort,
    "heap sort": heapSort
}


