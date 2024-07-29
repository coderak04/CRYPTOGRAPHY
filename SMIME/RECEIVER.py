import socket
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.Util.Padding import pad,unpad
import sys

def getKeys():
    #This function retures the private key of the receiver
    # and the public key of the sender.
    key= open('BobPrivateKey.pem', 'rb').read()
    key1= open('AlicePublicKey.pem','rb').read() 
    return RSA.importKey(key), RSA.importKey(key1)

def connectToServer():
    #This function is used to establish connection to the server
    #It returns the receiverSocket address of the server
    HOST=socket.gethostname()
    PORT=5556
    receiverSocket=socket.socket()
    print('Connecting to server...')
    try: 
        receiverSocket.connect((HOST, PORT))
    except socket.error as msg:
        print ('Bind failed.')
        sys.exit()
    return receiverSocket

def receiveMessage(receiverSocket, bobPrivateKey,alicePublicKey):
    #This function receives the following input:
    #1. receiverSocket: This is the socket address of the receiver (Bob)
    #2. bobPrivateKey: This is the private key of receiver Bob
    #3. alicePublicKey: This is the public key of sender Alice
    encryptedMessage=receiverSocket.recv(100000000)
    #Separating the different parts of the message
    splitMessage=encryptedMessage.split(b'\n\n\n\n\n')
    #Decrypt the one tine secret key 
    rsa=PKCS1_OAEP.new(bobPrivateKey)
    key = rsa.decrypt(splitMessage[0])
    #Now decrypting the message
    aes=AES.new(key, AES.MODE_CBC,splitMessage[1])
    messageSignature = aes.decrypt(splitMessage[2])
    messageAndSignature=unpad(messageSignature, AES.block_size) 
    originalEmail= messageAndSignature.split(b'\n\n\n\n\n')
    textEmail= originalEmail[0]
    #Creating the hash of the message to be verified. 
    textEmailHashed=SHA256.new(textEmail)
    #Verifying the signature of the sender. 
    keyVerifier=PKCS1_v1_5.new(alicePublicKey)
    if (keyVerifier.verify(textEmailHashed, originalEmail[1])):
        print("\nkey Verified")
        print('Recieved Email:', textEmail.decode())
    else:
        print('signature verification unsuccessful')

def closeConnection(recieverSocket):
    #This function is used to close the connection between the reciever and the server.
    recieverSocket.close()

print('This is the Reciever (Bob)')
bobPrivateKey, alicePublicKey = getKeys()
recieverSocket= connectToServer()
receiveMessage(recieverSocket, bobPrivateKey, alicePublicKey)   
closeConnection(recieverSocket)