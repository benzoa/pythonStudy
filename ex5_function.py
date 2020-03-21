# Global Functions ----------------------------------------------------------
print(dir(__builtins__))
print("=" * 40)

nums = list(range(5))
print("sum:", sum(nums))

def say_hello(para):
    print("Hello", para)

say_hello("World!")
print("True" if 'say_hello' in globals() else "False")
print("=" * 40)

# LGB Rules(Local -> Global -> Built-in) ------------------------------------
x = 50

def local_var(x):
    print("local_var x:", x)
    x = 20
    print("local_var x:", x)

def global_var():
    global x
    print("glbal_var x:", x)
    x = 10

local_var(x)
print('x:', x)

global_var()
print('x:', x)
print("=" * 40)

# deep copy & shallow copy --------------------------------------------------
def deep_copy(x):
    dx= x[:]
    dx[0] = 'Y'
    print("deep copy, x addr:", id(dx))

def shallow_copy(x):
    x[0] = 'Y'
    print("shallow_copy, x addr:", id(x))

wordlist = ['H', 'J', 'X']
print("worldlist addr:", id(wordlist))

deep_copy(wordlist)
print(wordlist)

shallow_copy(wordlist)
print(wordlist)
print("=" * 40)

# keyword argument ----------------------------------------------------------
def say(msg, times=1):
    print(msg * times)

say("Hello")
say("Hi ", 3)

def func(a, b=5, c=10):
    print('a: {:2d}, b: {:2d}, c: {:2d}'.format(a, b, c))

func(11)
func(3, 7)
func(23, c=22)
func(c=2, a=99)
print("=" * 40)

# variable argument ---------------------------------------------------------
def total(init=5, *nums, **keywords):
    print("init:", init)
    print("nums:", nums)
    print("keywords:", keywords)

    cnt = init
    for i in nums:
        cnt += i
    
    for key in keywords:
        cnt += keywords[key]
    
    return cnt

numbers = tuple(range(1, 10, 2))
shop_list = {"apple":40, "orange": 29}
print('total count:', total(10, *numbers, **shop_list))
print("=" * 40)

# recursive function  -------------------------------------------------------
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print("factorial(5):", factorial(5))
print("=" * 40)

# return value --------------------------------------------------------------
def maximum(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "same!"

print(maximum(10, 20), maximum(20, 10), maximum(10, 10), sep=", ")

# docstring -----------------------------------------------------------------
def print_max(x, y):
    ''' Prints the maximum of two numbers.

    The two values must be integers. '''
    print("type x: {}, y: {}".format(type(x), type(y)))

    if type(x) != int or type(y) != int:
        x = int(x)
        y = int(y)

    print(x if x > y else y, 'is maximum')

print_max("10", 20)
print("\nPrint : __doc__", "-" * 30)
print(print_max.__doc__)

print("\nPrint : docstring", '-' * 30)
help(print_max)
print("=" * 40)

# anonymous function(lambda expression) -------------------------------------
def mul(a, b): return a * b
def add(a, b): return a + b

def cal(pFunc, x, y):
    return pFunc(x, y)

print("mul:", cal(mul, 10, 20))
print("add:", cal(add, 10, 20))

tri = lambda x, y : x * y // 2
print("tri:", cal(tri, 10, 20))

print("lambda:", (lambda x, y : x * x / y)(5, 2))
print()

# map function --------------------------------------------------------------
# map(function, iterable, ...)
nums = list(range(1, 6))
print("nums:", nums)

mapped_nums = list(map(lambda x: x ** 2, nums))
print("mapped_nums:", mapped_nums)

exponents = list(range(1, 10, 2))
# print("exponents: {}".format(exponents))
answer = list(map(pow, mapped_nums, exponents))    # pow(x, y) : x^y
print("answer:", answer)

# filter function -----------------------------------------------------------
# filter(function, iterable)
func = lambda x: (x % 3) == 0
filtered_answer = list(filter(func, answer))
print("filtered:", filtered_answer)
print()

# sorted function  ----------------------------------------------------------
fruits = [
    ('apple', 40),
    ('orange', 20),
    ('mango', 10),
    ('pears', 26)
]

# sort(iterable, [, key][, reverse])
expensive_list = sorted(fruits, key = lambda x: x[1])
for i, price in enumerate(expensive_list):
    print("{}: {}".format(i, price))
