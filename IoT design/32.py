from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a)
sorted(a, key = itemgetter(0))
sorted(a, key = itemgetter(0, 1))
sorted(a, key = itemgetter(1))
sorted(a, key = itemgetter(1), reverse = True)