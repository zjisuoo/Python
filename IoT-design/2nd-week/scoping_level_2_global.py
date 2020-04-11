def outer() :
    test = 1 # outer scope
    def inner() : 
        global test
        test = 2 # nearest enclosing scope (which is 'outer')
        print('inner :', test)a

    inner()
    print('outer :', test)
    
test = 0 # gloabl scope
outer()
print('global :', test)