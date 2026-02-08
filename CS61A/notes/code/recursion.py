# from ucb import trace

def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    lugn_digit = sum_digits(2 * last)
    if n < 10:
        return lugn_digit
    else:
        return luhn_sum(all_but_last) + lugn_digit

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n != 0:
        f(n)
        g(n)

grow = lambda n : f_then_g(grow, print, n // 10)
shrink = lambda n : f_then_g(print, shrink, n // 10)

# @trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 2 + 4
# 1 + 1 + 4
# 3 + 3
# 1 + 2 + 3
# ...
# 1 + 1 + 1 + 1 + 1 + 1
# dp[n, m] = dp[n-m, m] + dp[n, m-1]
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m <= 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m



