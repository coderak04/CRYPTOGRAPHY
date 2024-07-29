import numpy as np
import matplotlib.pyplot as plt
from tinyec import registry
import secrets

# Parameters for the secp224r1 curve
ecc_curve = registry.get_curve('secp224r1')

# Generate a random private key
private_key = secrets.randbelow(ecc_curve.field.n)

# Calculate the corresponding public key
public_key = private_key * ecc_curve.g

# Plot the elliptic curve
a = 1
b = 1
ecc='1111'
y, x = np.ogrid[-7:7:100j, -7:7:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
plt.grid()

# Save the plot to a file
plt.savefig(ecc)
print("Saving curve to", ecc)

# Display the private and public keys
print("Private key: ", private_key)
print("Public key: ", public_key)

#Display the plot
plt.show()