age = 26
name = "python"

print("age: {}, name: {}".format(age, name))
print("{0} was {1} years old.".format(name, age))
print("job: {job}, money: {money}".format(money="1000", job="developer"))

person = {'name': 'ben', 'job': 'developer'}
print("name: {name}, job: {job}".format_map(person))

print("|{:>9}|{:^9}|".format(-10, 10))
print("|{0:_<9}|{0:*^9}|{0:#>9}|".format("ABC"))
print("{:,}".format(10000000))
print("{:3.2f}".format(4 / 3))
print("{0:.3f}, {0:0.3f}".format(4 / 3))

fval = format(4 / 3, ".3f")
print(fval)

print("{:e}".format(4 / 3))
print("{:.2%}".format(4 / 3))

print("{{ {:.2%} }}".format(10 / 3))
print("{}{}{}".format("{ ", "Hello", " }"))

print("x: {0:#x}, b: {0:#b}, o: {0:#o}, c: {1:c}".format(10, 65))

print("age: {age}".format(**globals()))
print('!s:{age!s}, !r:{age!r}, !a:{age!a}'.format(**globals()))

nums = [5, 4, 3, 2, 1]
print("nums[2]: {nums[2]}".format(**locals()))

class foo:
    var = 3.14

f = foo()
print("f.var: {f.var}".format(**vars()))

print(locals())
print("=" * 30)
print(vars())

words = ['spam', 'ham', 'eggs']
print("I like {0[2]}".format(words))

print("My name is {p[name]}".format(p=person))

from datetime import datetime
now = datetime.now()
print("Today is {0.year}-{0.month}-{0.day}".format(now))
print("Today is {:%Y-%m-%d %H:%M:%S}".format(now))
