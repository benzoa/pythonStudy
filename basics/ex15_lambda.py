# lambda expression(anonymous function)
plus_ten = lambda x : x + 10
'''
def plus_ten(x):
    return x + 10
'''
print("plus_ten(1): {}".format(plus_ten(1)))

call_self = (lambda x : x + 9)(1)
print("self1: {}".format(call_self))

y = 3
print("self2: {}".format((lambda : y)()))

plus_three = lambda x : x + y
print("plus_three(1): {}".format(plus_three(1)))

print("map: {}".format(list(map(plus_ten, range(5)))))

exp = lambda x: str(x) if x % 3 == 0 else x
values = list(range(1, 11))
print("conditional expression")
print("exp1: {}".format(list(map(exp, values))))

exp = lambda x: str(x) if x % 3 == 0 else float(x) if x % 2 == 0 else x
print("exp2: {}".format(list(map(exp, values))))

muls = list(range(11, 21))
exp = lambda x, y: x * y
print("exp3: {}".format(list(map(exp, values, muls))))

exp = lambda x: 3 < x < 8
print("filter: {}".format(list(filter(exp, values))))

from functools import reduce
exp = lambda x, y: x + y
print("reduce: {}".format(reduce(exp, values)))
