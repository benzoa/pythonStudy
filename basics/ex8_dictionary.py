email = {
    "kevin": "kevin@gmail.com",
    "john": "john@daum.net",
    "ben": "ben@naver.com"
}

print("len(email) : {} -> {}".format(len(email), email))

# typecasting to list, keys() and values() methods
print("list(email): {}".format(list(email)))
print("list(email.keys()): {}".format(list(email.keys())))
print("list(email.values()): {}".format(list(email.values())))

# sorted() method
print("sorted(email): {}".format(sorted(email)))
print("=" * 40)

# reference value by key
print("ben's email: {}".format(email['ben']))

for name in email:
    print(email[name])

for name, e_mail in email.items():
    print(" name: {}, email: {}".format(name, e_mail))

for i, name in enumerate(email):
    print("{}: {}, {}".format(i, name, email[name]))

print("=" * 40)

# update
email['ben'] = 'benzoa@gmail.com'

if 'ben' in email:
    print("ben's email: {}".format(email['ben']))

# add
email['kim'] = 'kim@naver.com'
print("email: {}".format(email))

# delete
del email['kevin']
print(email)

# clear
email.clear()
print("clear(): {}".format(email))
print("=" * 40)

'''
records = {
    "ben": 75,
    "kevin": 39,
    "john": 72
}
'''
records = dict(ben=75, kevin=39, john=72)

sum = 0
for val in records.values():
    sum += val

avg = round(sum / len(records))
print("sum: {}, avg: {}".format(sum, avg))
print("---------------------------")
print("| Name    | score | diff  |")
print("---------------------------")
fmt = "| {:<7} | {:>5} | {:^+5} |"

for name, val in sorted(records.items()):
    print(fmt.format(name, val, val - avg))

# function mapping
def add(a, b):
    return 'add : ' + str(a + b)

def sub(a, b):
    return 'sub : ' + str(a - b)

def mul(a, b):
    return 'mul : ' + str(a * b)

def div(a, b):
    return 'div : ' + str(a /b)

math_func = {'add':add, 'sub':sub, 'mul':mul, 'div':div}
print(math_func['add'](10, 20))

math_func_idx = {0:add, 1:sub, 2:mul, 3:div}
for i in range(4):
    print(math_func_idx[i](10, 20))
