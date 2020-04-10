from pprint import pprint

tdlist = [[1, 2], [3, 4], [5, 6]]
print("tdlist[1][1]: {}\n".format(tdlist[1][1]))

tdlist[2][1] = 10
print("double list")
pprint(tdlist, indent=4, width=20)

i = 0
fmt = "{}: {}, {}"

print("three ways to refer using for loop")
print("Type1")
for x, y in tdlist:  # list unpacking
    print(fmt.format(i, x, y))
    i += 1

print("\nType2")
k = 0
for i in range(len(tdlist)):
    print("{}: ".format(k), end="")
    for j in range(len(tdlist[i])):
        print("{} ".format(tdlist[i][j]), end="")
    
    print()
    k += 1

print("\nType3")
k = 0
for i in tdlist:
    print("{}: ".format(k), end="")
    for j in i:
        print("{} ".format(j), end="")
    
    print()
    k += 1

print("\nreference using while loop")
i = 0
while i < len(tdlist):
    x, y = tdlist[i] # list unpacking
    print(fmt.format(i, x, y))
    i += 1

print("\ntuple in the tuple")
tmp = ((1, 2), (3, 4), (5, 6))
pprint(tmp, indent=4, width=20)

print("\nlist in the tuple")
tmp = ([1, 2], [3, 4], [5, 6])
tmp[2][1] = 10
pprint(tmp, indent=4, width=20)

print("\ntuple in the list")
tmp = [(1, 2), (3, 4), (5, 6)]
tmp = [10, 20]
pprint(tmp, indent=4, width=20)
tmp.clear()
print("=" * 40)

# one-dimensional list
for i in range(5):
    tmp.append(i)

print("making one-dimensional list: {}".format(tmp))
tmp.clear()

# two-dimensional list
for i in range(3):
    add = []
    for j in range(4):
        add.append(j)
    
    tmp.append(add)

print("making two-dimensional list")
pprint(tmp, indent=4, width=20)
tmp.clear()

print("\nlist expression")
tmp = [i for i in range(10)]
print("one-dimensional: {}".format(tmp))
tmp.clear()

tmp = [[i for i in range(4)] for j in range(3)]
print("two-dimensional:")
print("Type1")
pprint(tmp, indent=4, width=20)
tmp.clear()

print("\nType2")
tmp = [[0] * 2 for i in range(3)]
pprint(tmp, indent=4, width=20)
tmp.clear()

print("=" * 40)

# jaged list
jlist = [
    [1, 2],
    [3, 4, 5], 
    [6],
    [7, 8, 9, 0]
]
print("\nJaged list")
pprint(jlist, indent=4, width=20)
jlist.clear()

print("\nDynamically Making Jaged list")
jlist.append([])
jlist[0].append("Ben")
jlist[0].append("Kevin")
jlist[0].append("Bob")

jlist.append([])
jlist[1].append(10)
jlist[1].append(20)
jlist[1].append(30)
jlist[1].append(40)

items = [i for i in range(3)]
jlist.append([])
jlist[2].extend(items)
pprint(jlist, indent=4, width=20)
