'''
스택 구현
class stack :
    def __init__(self) :
        self.stack_items = []

    def pop(self) :
        item_length = len(self.stack_items)

        if item_length < 1 :
            print("Stack is Empty!")
            return False 

        result = self.stack_items[item_length - 1]
        def self.stack_items[item_length - 1]
        return result
    
    def push(self, x) :
        self.stack_items.append(x)

    def isEmpty(self) :
        return not self.stack_items
'''

k = int(input())
money_stack = []

for i in range(k) :
    money = int(input())
    if money == 0 :
        del money_stack[-1]
    else :
        money_stack.append(money)

if not money_stack :
    print(0)
else :
    print(sum(money_stack))

try :
    1 <= k <= 10000
except ValueError :
    print ("Value Error")


