sang = int(input())
jung = int(input())
ha = int(input())
coke = int(input())
sprite = int(input())

set = [sang + coke, sang + sprite, jung + coke, jung + sprite, ha + coke, ha + sprite]
set.sort()

for sets in range(len(set)) :
    if sets == 0 :
        set[sets] = set[sets] - 50
        print(set[0]) 

try :
    100 <= sang, jung, ha, coke, sprite <= 2000
except ValueError :
    print ("Error Message")