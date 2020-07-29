while True :
    sen_stack = []
    sen = input()

    if sen == '.' :
        break

    for i in sen : 
        if i == '[' or i == '(' :
            sen_stack.append(i)
        elif i == ']' :
            try :
                if sen_stack[-1] == '[' :
                    sen_stack.pop()
                else :
                    print('no')
                    break
            except :
                print('no')
                break
        elif i == ')' :
            try :
                if sen_stack[-1] == '(' :
                    sen_stack.pop()
                else :
                    print('no')
                    break
            except :
                print('no')
                break
    else :
        if len(sen_stack) : 
            print('no')
        else : 
            print('yes')

