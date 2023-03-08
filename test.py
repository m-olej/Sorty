from GeneratorDanych import *
from sorts import *

listDict, sedgewickList = generator(10)


print(listDict['randList'])

print(selectionSort(listDict['randList']))

print(listDict['randList'])