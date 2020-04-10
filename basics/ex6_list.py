shopList = ["apple", "mango", "orange", "banana"]
print(dir(shopList))
print("=" * 40)

print("shopList len: ", len(shopList))

# enumerate(iterable, [, start=0])
for i, item in enumerate(shopList):
    print("{}: {}".format(i, item))

# reverse reference
print(shopList[-1], shopList[-2])

# append
shopList.append("carrot")
print(shopList)

# sorting
shopList.sort()
print(shopList)

# delete
del shopList[4]
print(shopList)

# update
shopList[0] = "pears"
print(shopList)

# list reference in the list
myList = ["kevin", 1, ["ben", 100]]
print("name:", myList[2][0], "money:", myList[2][1])

# global sum() function
nums = list(range(1, 11))
print("sum:", sum(nums))

# list division
lowScore = []
highScore = []

for num in nums:
    if num > 6:
        highScore.append(num)
    else:
        lowScore.append(num)

print("lowScore: {} -> {}".format(len(lowScore), lowScore))
print("highScore: {} -> {}".format(len(highScore), highScore))

# list merge
scores = lowScore + highScore
print("scores: {}".format(scores))

# += operator
scores += [11, 12, 13]
print("+= : {}".format(scores))

# extend(t) method
ext = [20, 21, 22]
scores.extend(ext)
print("extend:", scores)

# insert(i, x)
scores.insert(0, 99)
print("insert:", scores)

# remove(x)
scores.remove(1)
print("remove:", scores)

# pop([i])
print("pop:", scores.pop())
print(" -> ", scores)
print("pop:", scores.pop(1))
print(" -> ", scores)

# index() method
print("index({}): {}".format(20, scores.index(20)))
print("index({}): {}".format(20, scores.index(20, 5)))
print("index({}): {}".format(20, scores.index(20, 1, len(scores))))

# count(x)
print("count({}): {}".format(99, scores.count(99)))

# sort(key=function, reverse)
scores.sort()
print("sort:", scores)

def my_sort(x):
    # print(x[0])
    return x[0]

shopList.sort(key=my_sort)
print("sort(key=my_sort):", shopList)

# clear()
scores.clear()
print("clear:", scores)
