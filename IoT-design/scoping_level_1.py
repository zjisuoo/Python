def my_funcion() :
    test = 1 # this is defined in the local scope of the function
    print('my_function :', test)

test = 0 # this is defined in the global scope
my_funcion()
print('global :', test)