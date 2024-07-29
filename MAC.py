import hmac
import hashlib

#hmac
message=b'Welcome to Cryptography'
print(len(message))
key=b'CSI3002'
print(len(key))
hashfun=hashlib.sha1
hmac=hmac.new(message,key,hashfun).hexdigest()
print(hmac)

#md5 
    
mesg=b'Welcome'
key=b'Course'
hashval=hmac.new(mesg,key,hashlib.md5)
print("measage digest value is:")
print(hashval.digest())


#to apply for a file      

file="D:/College/Crypto/test.txt"#location of file
BLOCK_SIZE=65536 #size of each block read from the file
file_hash=hashlib.sha256()#create the hash object
with open(file,'rb') as f: # open the file to read its bytes
    fb=f.read(BLOCK_SIZE) # read from the file
    while len(fb) > 0:# while there is still data being read from the file
        file_hash.update(fb)# update the hash
        fb=f.read(BLOCK_SIZE) #read the next block from the file
print(file_hash.hexdigest()) #get the hexdigest of the hash'''