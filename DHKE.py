#Alice(A-sender) and Bob(B-receiver)
#X_A and X_B are private keys of A and B resp
#Y_A and Y_B are public keys of A and B resp
import math
#1) Choose a prime number q and an integer alpha such that
# alpha is a primitive root of q and alpha<q
q=23
alpha=5
#2) A and B select a random integer (X_A) and (X_B) resp such that X_A<q and X_B<q
X_A=6
X_B=15
print("DHKE Global Variables:")
print("Prime Number:",q)
print("Alpha:",alpha)
#3) A computes Y_A and B computes Y_B
Y_A=(alpha**X_A)%q
print("Alice sends through public channel Y_A:",Y_A)
Y_B=(alpha**X_B)%q
print("Bob sends through public channel Y_B:",Y_B)
print(f"User A's Private and Public Key:{X_A,Y_A}")
print(f"User B's Private and Public Key:{X_B,Y_B}")
#4) User A computes key as XA_K and User B computes key as XB_K
print("User A computes shared secret key:")
XA_K=(Y_B**X_A)%q
print("Alice Secret XA_K:",XA_K)
print("User B computes shared secret key:")
XB_K=(Y_A**X_B)%q
print("Bob secret XB_K:",XB_K)
print("Check whether XA_K and XB_K is same")
#5) They should be same
if XA_K==XB_K:
    print("They are same")
else:
    print("They are not same")