import lzma

with lzma.open('sample.xz', 'wt') as f:
    f.write('한국어 텍스트를 lzma 압축 파일에 쓰기')

with lzma.open('sample.xz', 'rt') as f:
    content = f.read()
    print(content)

text = '한국어 텍스트'
b = text.encode('utf-8')
lzma_data = lzma.compress(b)
print("len(b):", len(b))
print("len(lzma_data):", len(lzma_data))

long_text = b'A' * 10000
lzma_data = lzma.compress(long_text)
print("len(long_text):", len(long_text))
print("len(lzma_data):", len(lzma_data))

lzma_decompress_data = lzma.decompress(lzma_data)
print("len(lzma_decompress_data):", len(lzma_decompress_data))

if long_text == lzma_decompress_data:
    print("same")
else:
    print("different")