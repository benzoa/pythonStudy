import zlib

text = '한국어 테스트'
b = text.encode('utf-8')
compressed_data = zlib.compress(b)
print("len(b):", len(b))
print("len(compressed_data):", len(compressed_data))

long_text = b'A' * 10000
compressed_data = zlib.compress(long_text)
print("len(long_text):", len(long_text))
print("len(compressed_data):", len(compressed_data))

decompress_data = zlib.decompress(compressed_data)
print("len(decompress_data):", len(decompress_data))

if long_text == decompress_data:
    print("same")
else:
    print("different")
