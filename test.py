# from GeneratorDanych import *
# import random
from matplotlib import pyplot as plt


# listDict = generator(10000)

# qArray = listDict["descendList"][:]
# # print(qArray)

# testArr = [4, 14, 7, 2, 6, 10, 3, 8, 11, 5, 12, 6, 9]

# def Quicksort(arr):
    
#   if len(arr) <= 1:
#         return arr
  
#   stack = [(0, len(arr)-1)]

#   while stack:
      
#       left, right = stack.pop()
#       cut = partition(arr, left, right)
#       if cut > left:
#           stack.append((left, cut))
#       if cut + 1 < right:
#           stack.append((cut +1, right))
  
#   return arr


      

# def partition(arr, left, right):
#     pivot = arr[random.randint(left, right)]
#     i = left
#     j = right

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

# print(Quicksort(qArray))











# def iterative_quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     stack = [(0, len(arr)-1)]
    
#     while stack:
#         left, right = stack.pop()
#         pivot = partition(arr, left, right)
        
#         if pivot - 1 > left:
#             stack.append((left, pivot-1))
#         if pivot + 1 < right:
#             stack.append((pivot+1, right))
            
#     return arr
        
# def partition(arr, left, right):
#     pivot = arr[right]
#     i = left - 1
    
#     for j in range(left, right):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
    
#     arr[i+1], arr[right] = arr[right], arr[i+1]
    
#     return i+1


# print(iterative_quicksort(qArray))


quadX = [1, 2, 3, 4, 5]
quadY = [1, 4, 9, 16, 25]

linX = [1, 2, 3, 4, 5]
linY = [1, 2, 3, 4, 5]



fig, ax = plt.subplots()

ax.plot(quadX, quadY)
ax.plot(linX, linY)

plt.close()
plt.savefig("asda")