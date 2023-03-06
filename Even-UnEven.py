# unShapedList = []
even = []
uneven = []

for s in range(0 ,n, 2):
    even.append(s)

for t in range(1, n, 2):
    uneven.append(t)
uneven.reverse()

if len(even) > len(uneven):
    uneven.append(n)
    unShapedList = [sub[item] for item in range(len(uneven)) for sub in [even, uneven]]
    unShapedList2 = [sub[item] for item in range(len(uneven)) for sub in [uneven, even]]
    unShapedList.remove(n)
    unShapedList2.remove(n)
else:
    unShapedList = [sub[item] for item in range(len(uneven)) for sub in [even, uneven]]
    unShapedList2 = [sub[item] for item in range(len(uneven)) for sub in [uneven, even]]

# a-kształtne v.2
unShapedListv2 = even + uneven
# v-kształtne v.2
unShapedListv22 = uneven + even


# print(ascendList)
# print(descendList)
# print(aList)
# print(randList)
# print(constList)
# print('_________________')
