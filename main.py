from sorts import *
from GeneratorDanych import *
import time

graphData = []


for a in testSizeList:
    listDict = generator(a)
    for m, s in sortsDict.items():
      print(f"{m} {a} \n ----------------")
      for k, v in listDict.items():
        print(k)
        start = time.time_ns()
        s(v)
        end = time.time_ns()
        timeTaken = (end - start)/(10 ** 9)
        graphData.append([m, k, a, timeTaken])
        
# print(graphData)

selectionSortData = {"ascendList": [], "descendList": [], "randList": [], "aList": [], "constList": []}
insertionSortData = {"ascendList": [], "descendList": [], "randList": [], "aList": [], "constList": []}
shellSortData = {"ascendList": [], "descendList": [], "randList": [], "aList": [], "constList": []}
heapSortData = {"ascendList": [], "descendList": [], "randList": [], "aList": [], "constList": []}

sortDataList = [["selection sort" ,selectionSortData], ["insertion sort" ,insertionSortData], ["Sedgewick shell sort" ,shellSortData], ["heap sort" ,heapSortData]]

for d in range(len(graphData)):
   match graphData[d][0]:
      case "selection sort":
        match graphData[d][1]:
          case "ascendList":
            selectionSortData["ascendList"].append([graphData[d][2], graphData[d][3]])
          case "descendList":
            selectionSortData["descendList"].append([graphData[d][2], graphData[d][3]])
          case "randList":
            selectionSortData["randList"].append([graphData[d][2], graphData[d][3]])
          case "aList":
            selectionSortData["aList"].append([graphData[d][2], graphData[d][3]])
          case "constList":
            selectionSortData["constList"].append([graphData[d][2], graphData[d][3]])
          case _:
            print("oh oh")
      case "insertion sort":
        match graphData[d][1]:
          case "ascendList":
            insertionSortData["ascendList"].append([graphData[d][2], graphData[d][3]])
          case "descendList":
            insertionSortData["descendList"].append([graphData[d][2], graphData[d][3]])
          case "randList":
            insertionSortData["randList"].append([graphData[d][2], graphData[d][3]])
          case "aList":
            insertionSortData["aList"].append([graphData[d][2], graphData[d][3]])
          case "constList":
            insertionSortData["constList"].append([graphData[d][2], graphData[d][3]])
          case _:
            print("oh oh")
      case "Sedgewick shell sort":
        match graphData[d][1]:
          case "ascendList":
            shellSortData["ascendList"].append([graphData[d][2], graphData[d][3]])
          case "descendList":
            shellSortData["descendList"].append([graphData[d][2], graphData[d][3]])
          case "randList":
            shellSortData["randList"].append([graphData[d][2], graphData[d][3]])
          case "aList":
            shellSortData["aList"].append([graphData[d][2], graphData[d][3]])
          case "constList":
            shellSortData["constList"].append([graphData[d][2], graphData[d][3]])
          case _:
            print("oh oh")
      case "heap sort":
        match graphData[d][1]:
          case "ascendList":
            heapSortData["ascendList"].append([graphData[d][2], graphData[d][3]])
          case "descendList":
            heapSortData["descendList"].append([graphData[d][2], graphData[d][3]])
          case "randList":
            heapSortData["randList"].append([graphData[d][2], graphData[d][3]])
          case "aList":
            heapSortData["aList"].append([graphData[d][2], graphData[d][3]])
          case "constList":
            heapSortData["constList"].append([graphData[d][2], graphData[d][3]])
          case _:
            print("oh oh")
      case _:
        print("oh oh")


dataFile = open("data", "w")

for l in sortDataList:
  dataFile.write(l[0] + '\n')
  for k, v in listDict.items():
    dataFile.write(k + ":")
    for d in l[1][k]:
        strData = [str(x) for x in d]
        dataFile.write(",".join(strData) + ';')
    dataFile.write("\n")
  dataFile.write("\n")  




dataFile.close()