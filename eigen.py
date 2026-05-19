# Eigenvalues and Eigenvectors for 2x2 Matrix

print("Enter 2x2 Matrix:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

# Characteristic Equation
# λ² - (a + d)λ + (ad - bc) = 0

trace = a + d
determinant = (a * d) - (b * c)

# Discriminant
D = (trace * trace) - (4 * determinant)

# Square Root using exponent
sqrt_D = D ** 0.5

# Eigenvalues
lambda1 = (trace + sqrt_D) / 2
lambda2 = (trace - sqrt_D) / 2

print("\nEigenvalues:")
print("Lambda1 =", lambda1)
print("Lambda2 =", lambda2)

# Eigenvectors
print("\nEigenvector for Lambda1:")
print(f"[{b}, {lambda1 - a}]")

print("\nEigenvector for Lambda2:")
print(f"[{b}, {lambda2 - a}]")