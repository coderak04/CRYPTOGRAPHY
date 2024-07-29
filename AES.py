'''
#method1
from Crypto.Cipher import AES 
#eccryption key
key=b'C&F)H@McQfTjWnZr'
#create new instance of cipher
cipher=AES.new(key,AES.MODE_EAX)
#data to be encrypted
data='Welcome to the course on Cryptography!'.encode()
#nonce
nonce=cipher.nonce
#encrypt the data
ciphertext=cipher.encrypt(data)
print("Cipher text:",ciphertext)
#generate new instance with the key and nonce same as encyrption cipher
cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
#decrypt the data
plaintext=cipher.decrypt(ciphertext)
print("Plain text:",plaintext)
'''

#method2
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt(plaintext,key):
    cipher=AES.new(key,AES.MODE_ECB)
    padtext=pad(plaintext,AES.block_size)
    ctext=cipher.encrypt(padtext)
    encodedctext=base64.b64encode(ctext)
    return encodedctext

def decrpyt(ciphertext,key):
    cipher=AES.new(key,AES.MODE_ECB)
    decodedtext=base64.b64decode(ciphertext)
    padded_plaintext=cipher.decrypt(decodedtext)
    plaintext=unpad(padded_plaintext,AES.block_size)
    return plaintext

key=get_random_bytes(16)
plaintext=input('Enter the plain text:').encode()
enc=encrypt(plaintext,key)
print("Encrypted data is:",enc)
decrypted=decrpyt(enc,key)
print("Decrypted data is:",decrypted.decode('utf-8'))
