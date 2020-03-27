from math import sqrt
from random import randint

# run : > python ex13_module.py we play

num = 144
print("sqrt({}): {}".format(num, sqrt(num)))
print("randint(1, 100): {}".format(randint(1, 100)))
print("=" * 40)

type = True
importType = 3

if type:
    from sys import argv

    for i, arg in enumerate(argv):
        print("{}: {}".format(i, arg))
    
else:
    import sys

    for i, arg in enumerate(sys.argv):
        print("{}: {}".format(i, arg))

print("=" * 40)

if __name__ == '__main__':
    print("run: {}".format(__name__))

if importType == 1:
    from my_module import say_hi, __version__

    say_hi()
    print("ver: {}".format(__version__))
elif importType == 2:
    from my_module import *

    say_hi()
else:
    import my_module

    my_module.say_hi()
    print("ver: {}".format(my_module.__version__))

