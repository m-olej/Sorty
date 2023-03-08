from sorts import *
from GeneratorDanych import *
import time

graphData = []


for a in testSizeList:
    listDict = generator(a)
    for m, s in sortsDict.items():
      for k, v in listDict.items():
        start = time.time_ns()
        s(v)
        end = time.time_ns()
        timeTaken = (end - start)/(10 ** 9)
        graphData.append([m, k, a, timeTaken])
        
# print(graphData)

selectionSortData = []
insertionSortData = []
shellSortData = []
heapSortData = []

for d in range(len(graphData)):
   match graphData[d][0]:
      case "selection sort":
        selectionSortData.append(graphData[d][1:])
      case "insertion sort":
        insertionSortData.append(graphData[d][1:])
      case "Sedgewick shell sort":
        shellSortData.append(graphData[d][1:])
      case "heap sort":
        heapSortData.append(graphData[d][1:])
      case _:
        print("oh oh")



