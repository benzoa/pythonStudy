x = list(range(10))
print("dir(x): {}".format(dir(x)))

if '__iter__' in dir(x):
    print("True")

x_iter = x.__iter__()
print("x_iter.__(): {}".format(x_iter.__next__()))
print("x_iter.__(): {}".format(x_iter.__next__()))

class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            ret = self.current
            self.current += 1
            return ret
        else:
            raise StopIteration
    
for i in Counter(3):
    print(i, end=" ")

# iterator unpacking
x, y, z = Counter(3)
print("\nx: {}, y: {}, z: {}".format(x, y, z))

a, _, c = Counter(3)
print("a: {}, c: {}".format(a, c))

class Counter2:
    def __init__(self, stop):
        self.stop = stop
    
    def __getitem__(self, index):
        if index < self.stop:
            return index * 10   # 반환 값을 변형할 수 있음
        else:
            raise IndexError


print(Counter2(3)[0], Counter2(3)[1], Counter2(3)[2])

for i in Counter2(3):
    print(i, end=" ")

it = iter(range(3))
print("\nnext(it): {}".format(next(it)))
print("next(it): {}".format(next(it)))
print("next(it): {}".format(next(it)))

import random

it = iter(lambda : random.randint(0, 5), 2)
print("\nnext(it): {}".format(next(it)))
print("next(it): {}".format(next(it)))

it = iter(range(3))
print("next(it): {}".format(next(it, 10)))
print("next(it): {}".format(next(it, 10)))
print("next(it): {}".format(next(it, 10)))
