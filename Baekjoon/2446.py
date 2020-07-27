star = int(input())

for i in range(star) :
    print(" " * i + "*" * ((star - i) * 2 - 1))

for i in range(star - 2, -1, -1) :
    print(" " * i + "*" * ((star - i) * 2 - 1))

try :
    1 <= star <= 1000
except ValueError :
    print ("Error Message")