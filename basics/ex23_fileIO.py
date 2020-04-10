'''
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of the file if it exists
'b' binary mode
't' text mode (default)
'''


w_text = '''\
A palindrome is a word, number, phrase,
or other sequence of characters
which reads the same backward as forward, such as madam
'''

if __debug__:
    f = open("test.txt", "w")
    try:
        f.write(w_text)
    finally:
        f.close()

with open("test.txt", mode="w") as f:
    f.write(w_text)

f = open("test.txt")
print(f.read())
print("tell(): ", f.tell())
f.seek(0)

print(f.readlines())
f.seek(0)


while True :
    line = f.readline()
    if len(line) == 0:
        break

    print(line, end="")

f.close()

print("...............................")

with open("test.txt") as f:
    for line in f:
        print(line, end="")

print("\nKeyword Searching...........")
keyword = "backward"
with open("test.txt") as f:
    for i, line in enumerate(f):
        if line.find(keyword) >=0:
            print(i+1, ":", line)

print("\nMp3 Copying.................")
with open("canon_new_age_cpy.mp3", "wb") as f:
    f.write(open("canon_new_age2.mp3", "rb").read())

print("\nUsing Pickle Module.........")
import pickle

colors_list = ['red', 'green', 'blue']
with open('colors', 'wb') as f:
    pickle.dump(colors_list, f)

with open('colors', 'rb') as f:
    colors = pickle.load(f)

print(colors)