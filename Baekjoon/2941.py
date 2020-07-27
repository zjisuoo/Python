cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#print(cro)

cro_input = input()

for i in range(len(cro)) :
    #print(cro[i])
    cro_input = cro_input.replace(cro[i], str(i))

print(len(cro_input))