"""
STEPS:
1) Select 2 prime numbers (p and q) p!=q
2) Calculate n where n=p*q
3) Calcualte phi(n) where phi(n)=(p-1)(q-1)
4) Select 'e' such that 'e' is relatively prime to phi(n);
    gcd(phi(n),e)=1 and 1<e<phi(n)
5) Determine 'd' such that:
    d*e congruent modulo 1 mod phi(n)   
(We say integers a and b are "congruent modulo n" if their difference is a multiple of n.)

""" 
import math
#1) Select 2 prime numbers (p and q) p!=q
p=3
q=7
#2) Calculate n where n=p*q
n=p*q
print("n=",n)
#3) Calculate Euler's totient function
totient=(p-1)*(q-1)
#4) Select 'e' such that 'e' is relatively prime to totient function;
e=2
while(e<totient):
    if(math.gcd(e,totient)==1):
        break
    else:
        e+=1
print("e=",e)
#5) Calculate d where d*e congruent modulo to totient
k=2
d=((k*totient)+1)/e
print("d=",d)
print(f'Public key:{e,n}')
print(f'Private key:{d,n}')
#plain text
msg=11
print(f'Original message:{msg}')
#6) encryption process
c=pow(msg,e)
c=math.fmod(c,n)
print(f'Encrypted message:{c}')
#7) decryption process
m=pow(c,d)
m=math.fmod(m,n)
print(f'Decrypted Message:{m}')


