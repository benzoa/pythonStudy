x = 10
def foo():
    x = 20
    y = 10
    print("local locals(): {}\n".format(locals()))

foo()
print("global locals(): {}\n".format(locals()))


def print_hello():
    hello = "Hello, world!"

    def print_message():
        print(hello)
    print_message()

print_hello()


def A():
    x1 = 10
    def B():
        x1 = 20

    B()
    print('x1:', x1)

A()

def A():
    x2 = 10
    def B():
        nonlocal x2
        x2 = 20

    B()
    print('x2:', x2)

A()

def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x += 30
            y += 300
            print("x: {}, y: {}".format(x, y))
        C()
    B()

A()

x = 1
def A():
    x = 10

    def B():
        x = 20
        def C():
            global x
            x += 30
            print("x:", x)
        C()
    B()

A()

# closure
def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b

    return mul_add

c = calc()
print("c(2): {}, c(5): {}: ".format(c(2), c(5)))

def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total += a * x + b
        return total

    return mul_add

c = calc()
print("c(2): {}, c(5): {}\n".format(c(2), c(5)))

def lambda_calc():
    a = 3
    b = 5
    return lambda x: a * x + b

lambda_c = lambda_calc()
print("lambda_c(2): {}, lambda_c(5): {}".format(lambda_c(2), lambda_c(5)))
