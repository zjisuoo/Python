import random
import tqdm
from linear_algebra import vector_mean
from gradient_descent import gradient_step

def least_squares_fit(xs : List[Vector], 
            ys : List[float], 
            learning_rate : float = 0.001,
            num_steps : int = 1000,
            batch_size : int = 1) -> Vector :
    guess = [random.random() for _ in xs[0]]

    for _ in tqdm.trange(num_steps, desc = "least squares fit") :
        for start in range(0, len(xs), batch_size) :
            batch_xs = xs[start : start + batch_size]
            batch_ys = ys[start : start + batch_size]

            gradient = vector_mean([sqerror_gradient(x, y, guess)
                    for x, y in ziq(batch_xs, batch_ys)])
            guess = gradient_step(guess, gradient, -learning_rate)
    
    return guess
