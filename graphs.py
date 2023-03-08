from main import *
import matplotlib.pyplot as plt


# --- an example --- #
shellSortRandXData = []
shellSortRandYData = []

for x in range(len(shellSortData)):
    if shellSortData[0] == "randList":
        shellSortRandXData.append(shellSortData[1])
        shellSortRandYData.append(shellSortData[2])



plt.plot(shellSortRandXData, shellSortRandYData)
plt.xlabel('random shell sort')
plt.show()