q = 19
K = 17  # Replace this with the actual K value from your decryption step

# Calculate the multiplicative inverse of K modulo q
K_INV = pow(K, -1,q)

print("Multiplicative Inverse of K:", K_INV)
