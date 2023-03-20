# from main import *
from GeneratorDanych import factor
import matplotlib.pyplot as plt


dataRead = open('data', 'r')

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
        fig.savefig(sortG)
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
            # # plt.axex.set_autoscale_on(True)
            # plt.xlabel(f"skala: {str(factor)}")
            # plt.ylabel(f"in Seconds")
            # plt.savefig(f"./graphs/{sortG}-{ls[0]}")
            # plt.close()
            # --- for multiple graphs --- #
            ax.plot(x, y, label=ls[0])
            ax.legend(loc="upper left")
        print(f"{ls[0]}\n{x}\n{y}")
    i += 1