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
