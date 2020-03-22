d = {}
d['age'] = d.get('age', 0) + 1 # age not there, we get 0 + 1
d
d = {'age' : 39}
d['age'] = d.get('age', 0) + 1 # age is there, we get 40
d