d = {}
d['a'] = 1 # let’s set a couple of (key, value) pairs
d['b'] = 2
len(d) # how many pairs?
d['a']
d # how does ‘d’ look now?
del d['a'] # let’s remove ‘a’
d
d['c'] = 3 # let’s add ‘c’ : 3
'c' in d # membership is checked against the keys
3 in d # not the values
'e' in d
d.clear() # let’s clean everything from this dictionary
d