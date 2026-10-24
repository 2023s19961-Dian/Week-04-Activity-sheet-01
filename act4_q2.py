
import numpy as np

# (a) Define the coefficient matrix A
A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [3, 1, 2]
], dtype=float)

# Right-hand side vector B
B = np.array([10, 18, 17], dtype=float)

# (i) Determinant of A
print("(a)(i) Determinant of A:")
print(np.linalg.det(A))

# (ii) Inverse of A
print("\n(a)(ii) Inverse of A:")
print(np.linalg.inv(A))

# (iii) Eigenvalues of A
eigenvalues = np.linalg.eigvals(A)
print("\n(a)(iii) Eigenvalues of A:")
print(eigenvalues)

# (iv) Corresponding eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\n(a)(iv) Eigenvalues:")
print(eigenvalues)

print("Corresponding eigenvectors (columns):")
print(eigenvectors)

# (b) Solve AX = B
X = np.linalg.solve(A, B)
print("\n(b) Solution vector X = [x, y, z]:")
print(X)

# (c) Residual vector R = AX - B
R = A @ X - B
print("\n(c) Residual vector R:")
print(R)

# Euclidean norm of the residual
norm_R = np.linalg.norm(R, 2)
print("Euclidean norm ||R||_2:")
print(norm_R)
