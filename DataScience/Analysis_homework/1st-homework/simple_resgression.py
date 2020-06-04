from collections import Counter, defaultdict
from linear_algebra import vector_subtract
from stats import mean, correlation, standard_deviation, de_mean
from gradient_descent import minimize_stochastic
import math, random
import pandas as pd

data = pd.read_csv("./data2.csv", encoding = "utf-8")

train_nd = list()
test_nd = list()

train_ufdust = list()
test_ufdust = list()

for i in range(len(data)) :
    if i <= len(data) * 0.7 :
        train_nd.append(data['nd'][i])
        train_ufdust.append(data['ufdust'][i])
    else :
        test_nd.append(data['nd'][i])
        test_ufdust.append(data['ufdust'][i])

def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))

def least_squares_fit(x,y):
    """given training values for x and y,
    find the least-squares values of alpha and beta"""
    beta = correlation(train_nd, train_ufdust) * standard_deviation(train_ufdust) / standard_deviation(train_nd)
    alpha = mean(train_ufdust) - beta * mean(train_nd)
    return alpha, beta

def total_sum_of_squares(y):
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(train_ufdust))

def r_squared(alpha, beta, x, y):
    """the fraction of variation in y captured by the model, which equals
    1 - the fraction of variation in y not captured by the model"""

    return 1.0 - (sum_of_squared_errors(alpha, beta, train_nd, train_ufdust) / total_sum_of_squares(train_ufdust))

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),       # alpha partial derivative
            -2 * error(alpha, beta, x_i, y_i) * x_i] # beta partial derivative

# x = train_nd, y = train_ufdust
# x_i = test_nd, y_i = test_ufdust

if __name__ == "__main__":
    alpha, beta = least_squares_fit(train_nd, train_ufdust)

    print("alpha : ", alpha)
    print("beta : ", beta)

    print("r-squared : ", r_squared(alpha, beta, test_nd, test_ufdust))

    print()

    print("gradient descent : ")
    # choose random value to start
    random.seed(0)
    theta = [random.random(), random.random()]
    # theta = [test_nd, test_ufdust]
    alpha, beta = minimize_stochastic(squared_error, squared_error_gradient, train_nd, train_ufdust, theta, 0.0001)
    print("alpha : ", alpha)
    print("beta : ", beta)