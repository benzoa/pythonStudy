try:
    x = int(input("number: "))
    y = 10 / x
    print(y)
except:
    print("exception occured")

print("=" * 40)

val = [10, 20, 30]


'''
try:
    idx, x = map(int, input("index and number: ").split())
    print(val[idx] / x)
except ZeroDivisionError:
    print("The number cannot be divided by zero.")
except IndexError:
    print("Invalid index")
'''

'''
try:
    idx, x = map(int, input("index and number: ").split())
    print(val[idx] / x)
except ZeroDivisionError as e:
    print("error:", e)
except IndexError as e:
    print("error:", e)
'''

try:
    idx, x = map(int, input("index and number: ").split())
    print(val[idx] / x)
except Exception as e:
    print("error:", e)

print("=" * 40)

try:
    x = int(input("num: "))
    y = 10 / x
except ZeroDivisionError as e:
    print("error:", e)
else:
    print("result: {}".format(y))
finally:
    print("=" * 40)

'''
try:
    x = int(input("a multiple of three: "))
    if x % 3 != 0:
        raise Exception('It\'s not a multiple of 3.')
    print("x:", x)
except Exception as e:
    print("error:", e)
'''
'''
def three_multiple():
    x = int(input("a multiple of three: "))
    if x % 3 != 0:
        raise Exception('It\'s not a multiple of 3.')
    print("x:", x)

try:
    three_multiple()
except Exception as e:
    print("error:", e)
'''

def three_multiple():
    try:
        x = int(input("a multiple of three: "))
        if x % 3 != 0:
            raise Exception('It\'s not a multiple of 3.')
        print("x:", x)
    except Exception as e:
        print("e:", e)
        raise RuntimeError("Error in three_multiple") 

try:
    three_multiple()
except Exception as e:
    print("error:", e)

print("=" * 40)

x = int(input("a multiple of four: "))
assert x % 4 == 0, 'It\'s not a multiple of 4.'
print("x:", x)
print("=" * 40)

# Making Exception
# Type1
'''
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('It\'s not a multiple of 3.')

def three_multiple():
    try:
        x = int(input("a multiple of three: "))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('e:', e)


three_multiple()
'''

# Type2
class NotThreeMultipleError(Exception):
    pass

def three_multiple2():
    try:
        x = int(input("a multiple of three: "))
        if x % 3 != 0:
            raise NotThreeMultipleError('It\'s not a multiple of 3.')
        print(x)
    except Exception as e:
        print('e:', e)


three_multiple2()