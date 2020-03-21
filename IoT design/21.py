s = "This is unicode" # unicode string : code points
type(s)
encoded_s = s.encode('utf-8') # utf-8 encoded version of s
encoded_s
type(encoded_s) # another way to verify it
encoded_s.decode('utf-8') # let's revert to the original
bytes_obj = b"A bytes object" # a bytes object
type(bytes_obj)