def number_coroutine():
    while True:
        x = (yield)
        print(x)


co1 = number_coroutine()
next(co1)

co1.send(1)
co1.send(2)
co1.send(3)

# ------------------------------

def sum_coroutine():
    total = 0
    while True:
        x = (yield total)
        total += x

co2 = sum_coroutine()

print(next(co2))

print(co2.send(1))
print(co2.send(2))
print(co2.send(3))

# ------------------------------

def sum_coroutine2():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total
 
co3 = sum_coroutine2()
next(co3)
 
for i in range(20):
    co3.send(i)

print(co3.throw(RuntimeError, 'Break coroutine with exception'))

# ------------------------------

def accumulate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
        total += x
 
def sum_coroutine3():
    while True:
        total = yield from accumulate()
        print(total)
 
co4 = sum_coroutine3()
next(co4)
 
for i in range(1, 11):
    co4.send(i)
co4.send(None)
 
for i in range(1, 101):
    co4.send(i)
co4.send(None)

# ------------------------------

def accumulate2():
    total = 0
    while True:
        x = (yield)
        if x is None:
            raise StopIteration(total)
        total += x
 
def sum_coroutine2():
    while True:
        total = yield from accumulate2()
        print(total)
 
co5 = sum_coroutine2()
next(co5)
 
for i in range(1, 11):
    co5.send(i)
co5.send(None)
 
for i in range(1, 101):
    co5.send(i)
co5.send(None)
