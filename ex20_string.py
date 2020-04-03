# 문자열 변환 메서드 ..................................................
print("\nChanging String Methods..........")

# 1. replace(old, new [, count]) : old를 new로 치환, count 개수만큼
old = "This is a pen."
new = old.replace("pen", "note")    # 치환된 문자열이 저장
print("replace(): {}".format(new))
print(old)      # 원본은 유지
print("")

# 2. lower() : 소문자로 변환
print("lower(): {}".format(new.lower()))

# 3. upper() : 대문자로 변환
print("upper(): {}".format(new.upper()))

# 4. swapcase() : 대문자는 소문자로, 소문자는 대문자로 변환
print("swapcase(): {}".format(new.swapcase()))

# 5. capitalize() : 첫 번째 단어의 첫 글자는 대문자, 나머지 단어는 소문자로 변환
print("capitalize(): {}".format(new.capitalize()))

# 6. title() : 단어마다 첫 글자는 대문자, 나머지는 소문자로 변환
print("title(): {}".format(new.title()))

# 문자열 검사 메서드 ..................................................
print("\nChecking String Methods..........")

# 1. isnumeric() : 문자열 전체가 숫자로 구성되면 True 리턴
print("isnumeric(): {}".format(new.isnumeric()))

# 2. isalnum() : 문자열이 숫자와 문자일 때 True 리턴
print("isalnum(): {}".format("abc123".isalnum()))

# 3. isalpha() : 문자열이 문자일 때 True 리턴, 숫자나 기호가 포함되면 False
print("isalpha(): {}".format("abc123".isalpha()))

# 4. isdecimal() : 문자열이 10진수 때 True 리턴
print("isdecimal(): {}".format("123".isdecimal()))

# 5. isdigit() : 문자열이 숫자로만 이뤄져 있으면 True 리턴
print("isdigit(): {}".format("123".isdigit()))

# 6. isidentifier() : 식별자로 사용할 수 있는 문자열이면 True 리턴
print("isidentifier(): {}".format("abc123".isidentifier()))

# 7. islower() : 문자열이 모두 소문자면 True 리턴
print("islower(): {}".format("abc".islower()))

# 8. isprintable() : 문자열이 프린트 가능할 때 True 리턴
print("isprintable(): {}".format("abc123".isprintable()))

# 9. isspace() : 스페이스, 탭 등의 공백문자면 True 리턴
print("isspace(): {}".format(" ".isspace()))

# 10. istitle() : 첫 글자만 대문자고 뒤는 소문자인 문자열이면 True 리턴
print("istitle(): {}".format("Abc".istitle()))

# 11. isupper() : 문자열이 모두 대문자면 True 리턴
print("isupper(): {}".format("ABC".isupper()))

# 문자열 메서드 .......................................................
print("\nString Methods...................")

# 1. split(sep=None, maxsplit=-1) : 문자열 분할해서 리스트 반환, 공백 문자로 기준으로 분할
words = "ABC DEF AAA BBB CCC DDD EEE FFF"
print("words.split(): {}".format(words.split()))

text = "123:abc:!2$"
text = text.split(":")      # :으로 분할
print("split(\":\"): {}".format(text))

text = "2020/02/02"
text = text.split("/", maxsplit=1)      # maxsplit의 개수만큼 분할
print("split(\"/\"): {}".format(text))

# 2. find(sub, [, start [, end]]) : sub의 위치를 리턴, 없으면 -1 리턴
print("find(\"note\"): {}".format(new.find("note")))

# 3. strip([문자집합]) : 맨 앞 또는 맨 뒤의 문자집합과 일치하면 삭제하고 반환
print("strip(): {}".format(" abc ".strip()))        # abc, 앞뒤의 공백 문자를 삭제
print("strip(\"note.\"): {}".format(new.strip("note.")))
print("strip(\"This\"): {}".format(new.strip("This")))

# 4. startswith(prefix[, start[, end]]) : 지정된 접두사(prefix)로 시작되면 True 반환
print("startswith(\"This\"): {}".format(new.startswith("This")))

# 5. endswith(suffix[, start[, end]]) : 지정된 접미사를 가진 문자열 검색,
# suffix는 튜플로 여러개의 후보 지정 가능
image_suffix = ('jpg', 'png', 'gif')
print("endswith(image_suffix): {}".format('image.png'.endswith(image_suffix)))

# 6. join(iterable): 인수(list, tuple, set)로 지정된 여러 문자열을 결합
# list에는 join() 매서드가 없으므로 문자열의 join() 매서드를 사용한다.
fruitList = ["apple", "banana", "melon"]

# -로 리스트의 각 항목을 연결해서 문자열 생성, "연결문자열".join(리스트)
text = "-".join(fruitList)
print("\"-\".join(fruitList): {}".format(text))
