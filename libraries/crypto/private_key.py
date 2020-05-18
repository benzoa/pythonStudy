from Crypto.PublicKey import RSA

rsa = RSA.generate(2048)

# private key
private_pem = rsa.exportKey(format='PEM', passphrase='password')
with open('private.pem', 'wb') as f:
    f.write(private_pem)
