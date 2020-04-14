numbers = [1, 2, 3, 4, 5]
result_1 = []

for n in numbers :    
   if n % 2 == 1 :        
      result_1.append(n*2)

print(result_1)

result_2 = [i * 2 for i in numbers if i % 2 == 1]
print(result_2)
