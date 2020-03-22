a = dict(A = 1, Z = -1)
b = {'A' : 1, 'Z' : -1}
c = dict(zip( ['A', 'Z'], [1, -1] ))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z' : -1, 'A' : 1})
a == b == c == d == e # are they all the same?