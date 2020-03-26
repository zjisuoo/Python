a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

c = [[sum(i * f for i, j in zip(r, c)) for c zip(*b)]
    for r in a]