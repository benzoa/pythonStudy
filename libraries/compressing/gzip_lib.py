import gzip

with gzip.open('sample.gz', 'wt') as f:
    f.write('한국어 텍스트를 gzip 압축 파일로 저장')

with gzip.open('sample.gz', 'rt') as f:
    content = f.read()

print("content:", content)

text = '한국어 텍스트'
b = text.encode('utf-8')
gzipped_data = gzip.compress(b)

print("len(b):", len(b))
print("len(gzipped_data):", len(gzipped_data))

long_text = b'A' * 10000
gzipped_data = gzip.compress(long_text)
print("len(long_text):", len(long_text))
print("len(gzipped_data):", len(gzipped_data))

gunzipped_data = gzip.decompress(gzipped_data)
print("len(gunzipped_data):", len(gunzipped_data))

if long_text == gunzipped_data:
    print("same")
else:
    print("different")  
