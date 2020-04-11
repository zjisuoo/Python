def get_multiples_of_five(n) :
    return list(filter(lambda k : not k % 5, range(n)))