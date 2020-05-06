import random
from typing import TypeVar, List, Tuple

X = TypeVar('X')  
# generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]] :
    """Split data into fractions [prob, 1 - prob]"""    
    # (실습) Make a shallow copy    
    # (실습) because shuffle modifies the list.   
    # (실습) Use prob to find a cutoff    
    # (실습) and split the shuffled list there.
    data = [n for n in range(1000)]
    train, test = split_data(data, 0.75)
    # The proportions should be correct
    assert len(train) == 750
    assert len(test) == 250
    
    # And the original data should be preserved (in some order)
    assert sorted(train + test) == data

Y = TypeVar('Y')  # generic type to represent output variables

def train_test_split(xs: List[X], ys: List[Y],test_pct: float) -> Tuple[List[X], List[X], List[Y], 
List[Y]]:    
    # Generate the indices and split them.    
    idxs = [i for i in range(len(xs))]    
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)   

    return ([xs[i] for i in train_idxs],  # x_train            
            [xs[i] for i in test_idxs],   # x_test            
            [ys[i] for i in train_idxs],  # y_train            
            [ys[i] for i in test_idxs])   # y_test

    xs = [x for x in range(20)]  # xs are 1 ... 1000
    ys = [2 * x for x in xs]     # each y_i is twice x_i
    x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)
    
    print(xs, ys)
    print(x_train, x_test)
    print(y_train, y_test)
