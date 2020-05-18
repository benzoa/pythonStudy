from Crypto.PublicKey import RSA

rsa = RSA.generate(2048)

# public key
public_pem = rsa.publickey().exportKey()
with open('public.pem', 'wb') as f:
    f.write(public_pem)