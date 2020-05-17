# https://www.dlitz.net/software/pycrypto/
# pip install pycryto

from Crypto.Hash import MD5, SHA512
hash_md5 = MD5.new()    # MD5
hash_md5.update(b'hamegg')
print("hash_md5.hexdigest():", hash_md5.hexdigest())

hash_sha512 = SHA512.new()    # SHA512
hash_sha512.update(b'ham')
print("hash_sha512.hexdigest():", hash_sha512.hexdigest())

hash_md5 = MD5.new(b'hamegg')
print("hash_md5.hexdigest():", hash_md5.hexdigest())

hash_md5 = MD5.new(b'ham')
print("hash_md5.hexdigest():", hash_md5.hexdigest())

hash_md5.update(b'egg')
print("hash_md5.hexdigest():", hash_md5.hexdigest())

import hashlib

string = 'a'
encoded_string = string.encode()
print('encoded_string:', encoded_string)

hexdigest = hashlib.sha256(encoded_string).hexdigest()
print('type1 a:', hexdigest)

sha256 = hashlib.new('sha256')
sha256.update(encoded_string)
print('tyep2 a:', sha256.hexdigest())

string2 = 'a.'
encoded_string2 = string2.encode()
print('a.:', hashlib.sha256(encoded_string2).hexdigest())

hash_md5 = hashlib.md5(b'hamegg')
print('hash_md5.hexdigest():', hash_md5.hexdigest())