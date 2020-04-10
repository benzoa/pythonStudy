# tuple packing 
zoo = ('python', 'elephant', 'penguin')
# zoo = 'python', 'elephant', 'penguin'

print("len(zoo): {} -> {}".format(len(zoo), zoo))
print("zoo[:2]:", zoo[:2])
print("There is a {} in the car".format(zoo[2][1:4] + zoo[2][-2:] + zoo[1][0]))
print("zoo(0): {}, zool(1): {}, zoo(2): {}".format(len(zoo[0]), len(zoo[1]), len(zoo[2])))

for i, item in enumerate(zoo):
    print("{}: {}".format(i, item))

singleTone = (2, )
print("singleTone", singleTone, type(singleTone), sep=", ")

# tuple unpacking
myTuple = (29, 11, 12, 77, 29, 62)
cpyTuple = myTuple[2:4]

a, b = cpyTuple
print("a: {}, b: {}".format(a, b))

# index(), count() methods
print("index(77): {}, count(29): {}".format(myTuple.index(77), myTuple.count(29)))

# min(), max(), sum()
print("min: {}, max: {}, sum: {}".format(min(myTuple), max(myTuple), sum(myTuple)))

# expression
exp = tuple(i for i in range(10) if i % 2 == 1)
print("expression: {}".format(exp))

# typecating
fTuple = tuple(map(float, myTuple))
print("typecasting to float: {}".format(fTuple))
