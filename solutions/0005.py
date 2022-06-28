# 0005 [Medium]
# 2022-28-06
'''
This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(fun):
    return fun(lambda a, b: a)

def cdr(fun):
    return fun(lambda a, b: b)


print(car(cons(3, 4))) # should return 3
print(cdr(cons(3, 4))) # should return 4
