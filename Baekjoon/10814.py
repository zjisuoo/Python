n = int(input())
user_list = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    user_list.append((age, name))

user_list.sort(key = lambda user : (user[0]))

for user in user_list:
    print(user[0], user[1])