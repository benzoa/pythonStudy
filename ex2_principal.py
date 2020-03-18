import sys

# Variable
# 변수 : 자료형 선언 없음, 선언된 변수에 다른 타입의 변수를 입력하면 자동으로 타입이 변경됨
# 변수명 : 영문자와 숫자 조합, 대소문자 구분, 첫 글자는 소문자(숫자 불가!), '_' 시작 가능, 특수문자 & 키워드 불가
# python shell에서 직전 실행 결과는 '_' 변수에 저장

x = None    # empty
a = 1_000_000   # integer
b = 2
print("a + b:", a + b)

x, y = 1, 2     # tuple unpacking
y, x = x, y

c = d = 3
del x, y, c, d  # 삭제

f = 3.14    # 실수
s = "A"     # 문자열
t = True    # boolean
print("f:", f, "s:", s, "t:", t, sep=", ")

hex = 0x10  
oct = 0o10
bin = 0b10
print("hex: {}, oct: {}, bin: {}".format(hex, oct, bin))
print("=" * 30)

a = 2
a **= 10
print(a, -a)

print(10 / 3, 10 // 3, 10 % 3, sep=", ")
print(10.0 / 3, 10.0 // 3, 10.0 % 3, sep=", ")
print(10.0 / 3.0, 10.0 // 3.0, 10.0 % 3.0, sep=", ")

# divmode() : 몫과 나머지를 튜플로 반환
quotient, remainder = divmod(5, 2)
print("quotient: {}, remainder: {}".format(quotient, remainder))

a = 5.3E+2
b = 2.1E-3
print("5.3E+2:", a, "\n2.1E-3:", b)

print(int(3.14), int("10"), sep=", ")
print(float(3), float("3.14"), float(10 // 2), sep=", ")
print(str(3), str(3.14), sep=", ")

# 문자 <-> 유니 코드
print(ord('s'), chr(115))
print("=" * 30)

t1 = sys.maxsize    # 2147483647, 파이썬 2.7에서 변수에 담을 수 있는 가장 큰 수로 초과 시 long으로 변경
t2 = t1 + 1
t3 = t2 ** 10
print("t1: {0}, t2: {1}, t3: {2}".format(t1, t2, t3))
print(type(t1), type(t2), type(t3), sep=", ")   # 모두 int

print("abc 'def'", 'abc "def"', 'abc \'def\'', "abc \"def\"", sep=", ")

str1 = """abc
def"""
print("str1:", str1)

str2 = """abc \
def"""
print("str2:", str2)

str1 = '''문자열에 \'\'\' 사용'''
str2 = "ABC"
str3 = "DEF"
print("str1:", str1)
print("str2 + str3:", str2 + str3)

per_inch = 2.54
inch = 8
print(str(inch) + "inch: " + str(per_inch * inch) + "cm")

# print()의 default인자 : sep=" ", end="\n"
print("Hello ", end="") # 개행 막기
print("World")

print("a", "\n", "b")
print("a", "\n", "b", sep="")   # sep 사용은 b 앞에 공백 제거를 위해서
print("Raaa\nbbbb")
