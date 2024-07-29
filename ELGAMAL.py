import math
q=19
alpha=2
print(f"Global public elements:{q,alpha}")
X_A=5
Y_A=(alpha**X_A)%q
print("Y_A is ",Y_A)
print(f"Public key is {q,alpha,Y_A}")
M=17
k=2
K=(Y_A**k)%q
print("K value is ",K)
C1=(alpha**k)%q
print("C1 value is ",C1)
C2=(K*M)%q
print("C2 value is ",C2)
print(f"Cipher text is {C1,C2}")
#DECRYPTION
K=(C1**X_A)%q
print("Key value is ",K)
#Plain text
# Calculate the multiplicative inverse of K modulo q
K_INV = pow(K, -1, q)
M=(C2*K_INV)%q
print("Plain text is ",M)
