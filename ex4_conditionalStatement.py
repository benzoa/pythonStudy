num = 23

print("Match" if num == 23 else "Mismatch")

var = int(input("natual number: "))

if var == num:
    print("same")
elif var < num:
    print("smaller")
else:
    print("bigger")

if var > num and var < 40:
    print("{} is bigger than {} and smaller than 40".format(var, num))
elif 0 < var < num:
    print("{} is smaller than {}".format(var, num))
else:
    pass

print("-" * 40)
# False: '', "", [], (), {}, None, ...
if '':
    print("True")
else:
    print("False")
print("-" * 40)

# while & Break & Continue ------------------------------------------------
running = True
loopStat = False

while running:
    var = int(input("number: "))

    if var == 777:
        print("cheakey!")
        break
    elif var == num:
        print("same!")
        running = False
    elif var > num:
        print("bigger!")
    else:
        print("smaller!")
else:
    print("end loop")
    loopStat = True

if loopStat == True:
    print("Normal termination")
else:
    print("Abnormal termination")

print("-" * 40)

# infinite loop
while True:
    name = input("name: ")

    if name == "quit":
        break
    elif len(name) < 3:
        print("too short!")
        continue
    else:
        print("my name is", name)
        break

# range(start, stop, step)
seq = range(5)  # seq = range(0, 5, 1)
print(list(seq), tuple(seq))

seq = range(1, 10, 2)
print(tuple(seq))

for i in seq:
    print(i)

print("")

# multiplication table
for i in range(2, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))
    print()

for i in range(10):
    if i % 2 == 0 or i % 5 == 0:
        continue

    print(i)
