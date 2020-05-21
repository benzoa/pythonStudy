import bz2
'''
with bz2.open('sample.bz2', 'wt') as f:
    f.write('한국어 텍스트를 bz2 압축 파일에 쓰기')
'''
with bz2.open('sample.bz2', 'rt') as f:
    content = f.read()

print(content)

text = '한국어 텍스트'
b = text.encode('utf-8')
bz2_data = bz2.compress(b)

print("len(b):", len(b))
print("len(bz2_data):", len(bz2_data))

long_text = b'A' * 10000
bz2_data = bz2.compress(long_text)
print("len(long_text):", len(long_text))
print("len(bz2_data):", len(bz2_data))

bz2_decompress_data = bz2.decompress(bz2_data)
print("len(bz2_decompress_data):", len(bz2_decompress_data))

if long_text == bz2_decompress_data:
    print("same")
else:
    print("different")
