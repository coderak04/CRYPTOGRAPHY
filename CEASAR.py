"""
CEASAR CIPHER ALGORITHM
STEP 1: EXTRACT THE ASCII VALUE OF A CHARACTER
STEP 2: SUBTRACT 65 IN CASE OF UPPER CASE OR 97 FOR LOWER CASE LETTERS
STEP 3: ADD SHIFT VALUE OR KEY VALUE
STEP 4: PERFORM MODULO OPERATION(WITH 26)
STEP 5: AGAIN ADD 65 IN CASE OF UPPER CASE LETTERS OR 97 FOR LOWER CASE LETTERS
a ascii value=97 and A ascii value=65
ord function converts character into its ascii value
"""
def encryption(pltext,shift):
    encrypted=""
    for val in pltext:
        if(val.isupper()):
            encrypted+=chr((ord(val)-65+shift)%26+65)
        else:
            encrypted+=chr((ord(val)-97+shift)%26+97)
    return encrypted
def decryption(ciphertext,shift):
    decrypted=""
    for val in ciphertext:
        if(val.isupper()):
            decrypted+=chr((ord(val)-65-shift)%26+65)
        else:
            decrypted+=chr((ord(val)-97-shift)%26+97)
    return decrypted

plaintext=input("Enter plain text: ")
key=int(input("Enter key: "))
ciphertext=encryption(plaintext,key)
pt=decryption(ciphertext,key)
print("Plain text: ",plaintext)
print("Key: ",key)
print("Cipher text: ",ciphertext)    
print("Decrypted text: ",pt)