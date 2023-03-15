# from main import *
import matplotlib.pyplot as plt


dataRead = open('data', 'r')

i = 0
for line in dataRead:
    if i % 7 == 0:
        print(line)
        sortG = line[:-1]
    elif line == "\n":
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
        if len(x) != 0 and len(y) != 0:
            plt.plot(x, y)
            plt.title(f"{sortG} - {ls[0]}")
            plt.axis([0, max(x), 0, max(y)])
            plt.xlabel('1e5')
            plt.savefig(f"{sortG}-{ls[0]}")
            plt.close()
        print(f"{ls[0]}\n{x}\n{y}")
    i += 1