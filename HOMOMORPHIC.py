import random
p=2083
g=7
x=17
y=pow(g,x,p)
print(f"Private key is {x}")
print(f"Public key is {p},{g},{y}")

def encrypt(m,r):
    c1=pow(g,r,p)
    c2=(m*pow(y,r,p))%p
    return c1,c2

def decrypt(c1,c2):
    return (c2*pow(c1,-1*x,p))%p

#input for encryption and decryption
m=100
r=random.randint(1,p-1)
print(f"Message,Random_Number={(m,r)}")

c1,c2=encrypt(m,r)
print(f"Cipher text={(c1,c2)}")
print(f"Original message={decrypt(c1,c2)}")

#multiplicative homomorphic
m1=9
r1=random.randint(1,p-1)
m1_encrypted=encrypt(m1,r1)

m2=11
r2=random.randint(1,p-1)
m2_encrypted=encrypt(m2,r2)

h1=encrypt(m1*m2,r1*r2)
h2=m1_encrypted[0]*m2_encrypted[0]%p, m1_encrypted[1]*m2_encrypted[1]%p
print("Multiplicative Homomorphic")
print(h1,h2)

#additive homomorphic
m1=9
r1=random.randint(1,p-1)
m1_encrypted=encrypt(m1,r1)

m2=11
r2=random.randint(1,p-1)
m2_encrypted=encrypt(m2,r2)

h1=encrypt(m1+m2,r1+r2)
h2=m1_encrypted[0]*m2_encrypted[0]%p, m1_encrypted[1]*m2_encrypted[1]%p
print("Additive Homomorphic")
print(h1,h2)