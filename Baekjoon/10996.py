n = int(input())
even = n//2
odd = n - n//2

for i in range(n):
    print("* " * odd)
    print(" *" * even)