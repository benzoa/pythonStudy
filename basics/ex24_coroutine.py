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
