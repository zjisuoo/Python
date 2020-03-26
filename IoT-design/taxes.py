income = 15000
if income < 10000 :
    tax_cofficient = 0.0 # 1
elif income < 30000 :
    tax_cofficient = 0.2 # 2
elif income < 100000 :
    tax_cofficient = 0.35 # 3
else : 
    tax_cofficient = 0.45 # 4

print('I will pay:', income * tax_cofficient, 'in taxes')
