def print_nums(a, b, c):
	print("a: {}, b: {}, c: {}".format(a, b, c))

x = [11, 12, 13]
print_nums(*x)

def print_args(*args):
	for arg in args:
		print(arg)

print_args(10)
print_args(10, 20, 30)
print_args(*x)
print("=" * 40)

def print_nums(a, *args):
	print(a)
	print(args)

print_nums(1)
print_nums(1, 10, 20)
print_nums(*[10, 20, 30])
print("=" * 40)

def person_info(name, age, addr):
	print("name: {}".format(name))
	print("age: {}".format(age))
	print("addr: {}".format(addr))

person_info(name="홍길동", age=30, addr="서울시 강남구 삼성동")

# Dictionary Unpacking
x = {'name': '홍길동', 'age': 30, 'addr': '서울시 강남구 삼성동'}
person_info(**x)
person_info(**{'name': '홍길동', 'age': 30, 'addr': '서울시 강남구 삼성동'})

person_info(*x) # keyword
print("=" * 40)

def person_info2(**kwargs):
	for kw, arg in kwargs.items():
		print(kw, ': ', arg, sep='')

person_info2(name="Ben")
person_info2(name="Ben", age=30, addr="서울시 강남구 삼성동")

x = {'name': 'kevin'}
person_info2(**x)

x = {"name": "Ben", "age": 30, "addr": "서울시 강남구 삼성동"}
person_info2(**x)
print("=" * 40)
'''
def person_info(**kwargs):
	if 'name' in kwargs:
		print("name: {}".format(kwargs['name'])
	if 'age' in kwargs:
		print("age: {}".format(kwargs['age'])
	if 'addr' in kwargs:
		print("addr: {}".format(kwargs['addr'])
'''

def person_info3(name, **kwargs):
	print(name)
	print(kwargs)

person_info3("Ben")
person_info3("Ben", age=30, addr="서울시 강남구 삼성동")
person_info3(**{"name" : "Ben", "age" : 30, "addr" : "서울시 강남구 삼성동"})

def custom_print(name, *args, **kwargs):
	print(name, *args, **kwargs)

custom_print("Ben", 1, 2, 3, sep=" : ", end='')
