import pandas as pd
from typing import TypeVar, List, Tuple
X = TypeVar('X')
from functools import partial
from scratch.linear_algebra import dot, vector_add, Vector
import tqdm
from scratch.probability import normal_cdf
from scratch.gradient_descent import minimize_stochastic
from scratch.simple_linear_regression import total_sum_of_squares
import math, random

import tqdm
from scratch.linear_algebra import vector_mean
from scratch.gradient_descent import gradient_step

import numpy as np

def predict(x_i, beta):
    return dot(x_i, beta)

def error(x_i: Vector, y_i:float, beta: Vector) -> float:
    return predict(x_i, beta) - y_i

def squared_error(x_i:Vector, y_i:float, beta:Vector)->float:
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i:Vector, y_i:float, beta:Vector)->Vector:
    """the gradient corresponding to the ith squared error term"""
    err = error(x_i, y_i, beta)
    return [2* err * x for x in x_i]

def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error,
                               squared_error_gradient,
                               x, y,
                               beta_initial,
                               0.001)

def multiple_r_squared(x:List[Vector], y:Vector, beta:Vector) ->float:
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2
                                for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

def bootstrap_sample(data):
    """randomly samples len(data) elements with replacement"""
    return [random.choice(data) for _ in data]

def bootstrap_statistic(data, stats_fn, num_samples):
    """evaluates stats_fn on num_samples bootstrap samples from data"""
    return [stats_fn(bootstrap_sample(data))
            for _ in range(num_samples)]

def estimate_sample_beta(sample):
    x_sample, y_sample = list(zip(*sample)) # magic unzipping trick
    return estimate_beta(x_sample, y_sample)

def p_value(beta_hat_j, sigma_hat_j):
    if beta_hat_j > 0:
        return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
    else:
        return 2 * normal_cdf(beta_hat_j / sigma_hat_j)

#
# REGULARIZED REGRESSION
#

# alpha is a *hyperparameter* controlling how harsh the penalty is
# sometimes it's called "lambda" but that already means something in Python
def ridge_penalty(beta, alpha):
  return alpha * dot(beta[1:], beta[1:])

def squared_error_ridge(x_i, y_i, beta, alpha):
    """estimate error plus ridge penalty on beta"""
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)

def ridge_penalty_gradient(beta, alpha):
    """gradient of just the ridge penalty"""
    return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]

def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
    """the gradient corresponding to the ith squared error term
    including the ridge penalty"""
    return vector_add(squared_error_gradient(x_i, y_i, beta),
                      ridge_penalty_gradient(beta, alpha))

def estimate_beta_ridge(x, y, alpha):
    """use gradient descent to fit a ridge regression
    with penalty alpha"""
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(partial(squared_error_ridge, alpha=alpha),
                               partial(squared_error_ridge_gradient,
                                       alpha=alpha),
                               x, y,
                               beta_initial,
                               0.001)

def lasso_penalty(beta, alpha):
    return alpha * sum(abs(beta_i) for beta_i in beta[1:])

def split_data(data:List[X], prob: float) -> Tuple[List[X], List[X]]:
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob)
    return data[:cut], data[cut:]

def z_score_normalize(lst):
    normalized = []
    count=0
    print("doing")
    for value in lst:
        normalized_num = (value - np.mean(lst)) / np.std(lst)
        normalized.append(normalized_num)
        print("done ", count)
        count+=1
    return normalized


if __name__ == "__main__":
    df_data = pd.read_csv('data2.csv', encoding='cp949')
    data_list = df_data.values.tolist()

    data_list = [[cdate, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sagas, fdust_re, ufdust_re, ozone_re, nd_re, cm_re, sagas_re]
                 for (cdate, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sagas, fdust_re,ufdust_re, ozone_re, nd_re,cm_re, sagas_re) in data_list]

    train, test = split_data(data_list, 0.7)
    x_train = []
    y_train = []    # ufdust
    x_test = []
    y_test = []     # ufdust


    #train
    for i in range(0,len(data_list)):
        y_train.append(float(data_list[i][12]))

    for i in range(0,len(data_list)):
        x_train.append([float(data_list[i][11]), float(data_list[i][13]),float(data_list[i][14]),float(data_list[i][15]),float(data_list[i][16])])


    #test
    for i in range(0,len(data_list)):
        y_test.append(data_list[i][12])

    for i in range(0,len(data_list)):
        x_test.append([data_list[i][11], data_list[i][13], data_list[i][14], data_list[i][15], data_list[i][16]])

    random.seed(0)

    beta_train = estimate_beta(x_train, y_train)
    print("train : beta", beta_train)

    train_model = []

    for i in range(0, len(x_train)):
        train_model.append((beta_train[0]*x_train[i][0] + beta_train[1]*x_train[i][1] + beta_train[2]*x_train[i][2] + beta_train[3]*x_train[i][3] + beta_train[4]*x_train[i][4]))

    print("train : r-squared", multiple_r_squared(x_train, y_train, beta_train))
    #print(train_model)


    test_model = []
    beta_test =  estimate_beta(x_test, y_test)
    print("test : beta", beta_test)
    for i in range(0, len(x_train)):
        test_model.append((beta_test[0]*x_test[i][0] + beta_test[1]*x_test[i][1] + beta_test[2]*x_test[i][2] + beta_test[3]*x_test[i][3] + beta_test[4]*x_test[i][4]))
    print("test : r-squared", multiple_r_squared(x_test, y_test, beta_test))
    #print(test_model)




