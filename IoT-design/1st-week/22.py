s = "The trouble is you think you have time."
s[0] # indexing at position 0, which is the first char
s[5] # indexing at position 5, which is the sixth char
s[ : 4] # slicing, we specify only the stop position
s[4 : ] # slicing, we specify only the start position
s[2 : 14] # slicing, start, stop and step (every 3 chars)
s[ : ] # quick way of making a copy 