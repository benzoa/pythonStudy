from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

public_key_file = open('public.pem', 'r')
private_key_file = open('private.pem', 'r')

public_key = RSA.importKey(public_key_file.read())
private_key = RSA.importKey(private_key_file.read(), passphrase='password')
public_key_file.close()
private_key_file.close()

# encryption
print("original:", 'ham')

encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(b'ham')
print('encrypted:', encrypted)

# decryption
decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(encrypted)
print('decrypted:', decrypted.decode('utf8'))
