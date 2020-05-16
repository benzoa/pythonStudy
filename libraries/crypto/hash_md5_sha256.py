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
