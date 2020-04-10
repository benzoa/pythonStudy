colors = {"red", "green", "blue"}
print(colors)

if 'green' in colors:
    print("True")

e = set()
print(e)

a = set(range(5))
b = set('apple')
print("a: {}, b: {}".format(a, b))

fruits = set({"orange", "banana", "mango"})
outOfStock = {'banana'}
print("fruits: {}, outOfStock: {}".format(fruits, outOfStock))

print("\nunion")
print("colors | fruits: {}".format(colors | fruits))
print("set.union(colors | fruits) : {}".format(set.union(colors | fruits)))
print("colors.union(fruits) : {}\n".format(colors.union(fruits)))

print("intersection")
print("colors & fruits: {}".format(colors & fruits))
print("outOfStock & fruits: {}".format(outOfStock & fruits))
print("outOfStock.intersection(fruits): {}".format(outOfStock.intersection(fruits)))
print("set.intersection(outOfStock, fruits): {}\n".format(set.intersection(outOfStock, fruits)))

print("difference")
print("fruits - outOfStock: {}".format(fruits - outOfStock))
print("set.difference(fruits, outOfStock): {}\n".format(set.difference(fruits, outOfStock)))

print("symmetric difference")
print("outOfStock ^ fruits: {}".format(outOfStock ^ fruits))
print("set.symmetric_difference(outOfStock, fruits): {}\n".format(set.symmetric_difference(outOfStock, fruits)))

# union and allocation
colors |= {'sky'}
print("colors |= {{'sky'}}: {}".format(colors))

colors.update({'yellow'})
print("colors.update({{'yellow'}}): {}\n".format(colors))

# intersection and allocation
colors &= {'sky', 'yellow', 'green'}
print("colors &= {{'sky', 'yellow'}}: {}".format(colors))

colors.intersection_update({'yellow', 'sky'})
print("colors.difference_update({{'yellow', 'sky'}}): {}\n".format(colors))

# difference and allocation
colors -= {'sky'}
print("colors -= {{'sky'}}: {}".format(colors))

colors.difference_update({'yellow'})
print("colors.difference_update({{'yellow'}}): {}".format(colors))

colors ^= {'green'}
print("colors -= {{'green'}}: {}".format(colors))

colors.symmetric_difference_update({'red'})
print("colors.symmetric_difference_update({{'red'}}): {}\n".format(colors))

a = {1, 2, 3, 4}
b = {1, 2, 3, 4, 5}

if a <= b:
    print("a is subset of b")

if a.issubset(b):
    print("a is subset of b")

if a < b:
    print("a is proper subset of b")

if b >= a:
    print("b is superset of a")

if b.issuperset(a):
    print("b is superset of a")

if b > a:
    print("b is proper subset of a")

if a != b:
    print("a and b are difference")

if a.isdisjoint(b):
    print("isdisjoint: False")

a.add(10)
print("a.add(10):", a)

a.remove(3)
print("a.remove(3):", a)

a.discard(4)
print("a.discard(4):", a)

a.discard(7)
print("a.discard(7):", a)

pop_val = a.pop()
print("a.pop():", a, "pop val:", pop_val)

a.clear()
print("a.clear():", a)

print("len(b):", len(b))

a = b
print("a:", a)

a.add(10)
print("a.add(10):", a, "b:", b)

c = a.copy()
c.add(20)
print("c.add(20):", c, "a:", a)

for i in c:
    print(i)

a = {i for i in "apple"}    # a = set(i for i in "apple")
print("set expression1:", a)

a = {i for i in 'pineapple' if i not in 'apl'}
print("set expression2:", a)