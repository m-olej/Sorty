from GeneratorDanych import *


listDict = generator(10000)

qArray = listDict["descendList"][:]

def iterative_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr)-1)]
    
    while stack:
        left, right = stack.pop()
        pivot = partition(arr, left, right)
        
        if pivot - 1 > left:
            stack.append((left, pivot-1))
        if pivot + 1 < right:
            stack.append((pivot+1, right))
            
    return arr
        
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    return i+1


print(iterative_quicksort(qArray))