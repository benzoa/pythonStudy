def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

g = number_generator()
print("dir(g): {}".format(dir(g)))

'''
print("g.__next__(): {}".format(g.__next__()))
print("g.__next__(): {}".format(g.__next__()))
print("g.__next__(): {}".format(g.__next__()))
'''
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))

def one_generator():
    yield 1
    return 'return 0'

try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)

# range()처럼 동작하는 제너레이터 만들기
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

for i in number_generator(3):
    print(i)

g = number_generator(3)
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))
print("=" * 40)

def upper_generator(x):
    for i in x:
        yield i.upper()

fruits = ['apple', 'pear', 'grape', 'pineapple', 'mango']

for i in upper_generator(fruits):
    print(i)

def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i

for i in number_generator():
    print(i)

print("=" * 40)


def number_generator():
    x = [1, 2, 3]
    yield from x

for i in number_generator():
    print(i)

g = number_generator()
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))
print("next(g): {}".format(next(g)))

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3)

for i in three_generator():
    print(i)
