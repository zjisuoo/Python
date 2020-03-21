d
d.popitem() # removes a random item (useful in algorithms)
d
d.pop(‘1’) # remove item with key ‘1’
d.pop(‘not-a-key’) # remove a key not in dictionary : KeyError
d.pop(‘not-a-key’, ‘default-value’) # with a default value?
d.update({‘another’ : ‘value’}) # we can update dict this way
d.update(a = 13) # or this way (like a function call)
d
d.get(‘a’) # same as d[‘a’] but if key is missing no KeyError
d.get(‘a’, 177) # default value used if key is missing
d.get(‘b’, 177) # like in this case
d.get(‘b’) # key is not there, so None is returned