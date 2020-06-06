from collections import Counter
from functools import partial
from linear_algebra import dot, vector_add
from statistics import median, standard_deviation
from probability import normal_cdf
from gradient_descent import minimize_stochastic
from simple_linear_regression import total_sum_of_squares
import math, random
import pandas as pd
import numpy as np

data = pd.read_csv("./data2.csv", encoding = "utf-8")

train_nd = list()
test_nd = list()

train_fdust = list()
test_fdust = list()

train_ufdust = list()
test_ufdust = list()

for i in range(len(data)) :
    if i <= len(data) * 0.7 :
        a = list()
    
        a.append(data['nd'][i].item())
        train_nd.append(a)

        b = list()
        b.append(data['fdust'][i].item())
        train_fdust.append(b)

        train_ufdust.append(data['ufdust'][i].item())
    else :
        test_fdust.append(data['fdust'][i].item())
        test_nd.append(data['nd'][i].item())
        test_ufdust.append(data['ufdust'][i].item())

# 데이터 정규화 (1)
def z_score_normalized(val) :
    zNormalized = list()
    for value in val :
        zNormalized_num = (value - np.mean(val)) / np.std(val)
        zNormalized.append(round(zNormalized_num, 3))
    return zNormalized

# 데이터 정규화 (2)
def MinMaxScaler(val) :
    numerator = val - np.min(val, 0)
    denominator = np.max(val, 0) - np.min(val, 0)
    return numerator / (denominator + 1e-7)

def predict(x_i, beta):
    return dot(x_i, beta)

def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
    """the gradient corresponding to the ith squared error term"""
    return [-2 * x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]

def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x]
    return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, 0.001)

def multiple_r_squared(x, y, beta):
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
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
    return vector_add(squared_error_gradient(x_i, y_i, beta), ridge_penalty_gradient(beta, alpha))

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

if __name__ == "__main__":

    random.seed(0)
    beta = estimate_beta(train_nd, train_ufdust)
    print("Beta : ", beta)
    print("R-squared : ", multiple_r_squared(train_nd, train_ufdust, beta))