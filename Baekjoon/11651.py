n = int(input())

xy_list = []

for i in range(n) :
    [x, y] = map(int, input().split())
    re_list = [y, x]
    xy_list.append(re_list)

xy_list = sorted(xy_list)

for i in range(n) :
    print(xy_list[i][1], xy_list[i][0])