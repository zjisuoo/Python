star = int(input())

for i in range(1, star + 1, 1) :
    print('*' * i)

for i in range(star + 1, 0 , -1) :
    print('*' * i)

try :
    1 <= star <= 1000
except ValueError :
    print ("Error Message")