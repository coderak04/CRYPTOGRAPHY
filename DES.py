#method 1
'''
from Crypto.Cipher import DES
key=b'shhhhhh!'
OrigText=b'The US Navy has submarines in Kingsbay!!'
des=DES.new(key,DES.MODE_ECB)
'''
#method 2
from Crypto.Cipher import DES
key=b'hello123'
def pad(text):
    while(len(text)%8!=0):
        text+=b" "
    return text
des=DES.new(key,DES.MODE_ECB)
text=b'Welcome to the Course on Cryptography!'
padded_text=pad(text)
encrypted_text=des.encrypt(padded_text)
print(encrypted_text)
decrypted_text=des.decrypt(encrypted_text)
print(decrypted_text)