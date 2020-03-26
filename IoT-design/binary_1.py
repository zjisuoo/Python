n = 39
remainders = []
while n > 0 :
    remainder = n % 2 # remainder of division by 2
    remainders.insert(0, remainder) # we keep track of remainders
    n //= 2 # we divide n by 2

print(remainders)