from functools import reduce


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


# factorial(1) → 1
# factorial(2) → 2
# factorial(5) → 120


def sum(ls):
    acc = 0
    for i in ls:
        acc = acc + i
    return acc


def product(ls):
    acc = 1
    for i in ls:
        acc = acc * i
    return acc


# def accumlator_pattern(ls): # look at sum(ls) and product(ls) → this is a template for both models
#     acc = initial_value
#     for i in ls:
#         acc = f(acc, i)
#     return acc


# def aggregation_with_reduce(ls): # basically a template to use reduce
#     return reduce(f, ls, initial_value)


## convert sum function by using reduce
def sum1(ls):
    return reduce(lambda acc, i: acc + i, ls, 0)


## convert sum function by using reduce
def product1(ls):
    return reduce(lambda acc, i: acc * i, ls, 1)


def flat_map(f, s):
    for i in s:
        for j in f(i):
            yield j


def numbers(i):
    return [i - 1, i + 1]


# numbers(3) → [2, 3, 4]
# numbers(100) → [99, 100, 101]

# list(map(numbers, [1, 2, 3])) → [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
# list(flat_map(numbers, [1, 2, 3])) → [[0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4, 5]
