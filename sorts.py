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
  for j in range(1, len(array)):
    while j > 0 and array[j] < array[j-1]:
       temp = array[j-1]
       array[j-1] = array[j]
       array[j] = temp
       j -= 1


def shellSort(array, sedwick_list):
    new_array = list(array)
    for val in sedwick_list:
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


def quickSort(array, i, j, pivot):
    while i < len(array):
        while array[pivot] >= array[i]: i+=1
        while array[pivot] >= array[j]: j-=1
        if

