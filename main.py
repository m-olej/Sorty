from sorts import *
from GeneratorDanych import *
import time


# --- Selection sort --- #
selectionSortTimes = {}
for a in testSizeList:
    listDict = generator(a)
    for k, v in listDict.items():
      kopia = list(v)
      print(f"Unsorted {k}: {v}")
      start = time.time()
      selectionSort(v)
      end = time.time()
      selectionSortTimes[a] = end - start
      print(f"Sorted {k} by Selection sort \n {selectionSort(v)}")

print(selectionSortTimes)
