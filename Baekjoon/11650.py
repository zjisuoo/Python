n = int(input())

xy_list = []

for _ in range(n) :
    [x, y] = map(int, input().split())
    xy_list.append((x, y))

xy_list.sort()
xy_list.sort(key = lambda x : x[0])

for i in xy_list :
    print(*i)