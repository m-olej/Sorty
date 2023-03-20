# from main import *
from GeneratorDanych import factor
import matplotlib.pyplot as plt


dataRead = open('compData', 'r')

i = 0
for line in dataRead:
    if i % 7 == 0:
        currGraph = line
        print(line)
        sortG = line[:-1]
        # --- for multiple graphs --- #
        fig, ax = plt.subplots()
        ax.set_title(line)

    elif line == "\n":
        # --- for multiple graphs --- #
        # # tu możesz zmieniać nazwe do jakiego pliku zapisać, jeśli jest już plik o tej nazwie to nadpisze go 
        fig.savefig(sortG)
        # tego nie tykaj #
        pass
    else:
        ls = line.split(':')
        xy = ls[1].split(';')
        xy = xy[:-1]
        x = []
        y = []
        for v in xy:
            temp = v.split(',')
            x.append(temp[0])
            y.append(temp[1])
        x = [int(x)/factor for x in x]
        y = [float(y) for y in y]
        
        if len(x) != 0 and len(y) != 0:
            # --- for single graphs --- #
            # plt.plot(x, y)
            # plt.title(f"{sortG} - {ls[0]}")
            # plt.xlabel(f"skala: {str(factor)}")
            # plt.ylabel(f"in Seconds")
            # # tu możesz zmieniać nazwe do jakiego pliku zapisać, jeśli jest już plik o tej nazwie to nadpisze go 
            # plt.savefig(f"./graphs/{sortG}-{ls[0]}")
            # plt.close()
            # --- for multiple graphs --- #
            ax.plot(x, y, label=ls[0])
            ax.set_xlabel(f"skala: {str(factor)}")
            ax.set_ylabel(f"in Seconds")
            ax.legend(loc="upper left")
        print(f"{ls[0]}\n{x}\n{y}")
    i += 1

dataRead.close()

# comparing sorts on same test lists #

