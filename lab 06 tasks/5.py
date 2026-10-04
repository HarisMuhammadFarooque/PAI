import numpy as np

A = np.array([[1, 4, 7],
              [2, 1, 9],
              [5, 0, 2]])

B = np.array([[2, 7, 2],
              [5, 1, 3],
              [9, 0, 4]])

def show_shapes():
    print(f"Shapes -> A: {A.shape}, B: {B.shape}")

# Addition, subtraction, element-wise multiplication:
# need the SAME shape (or shapes that can broadcast)
show_shapes()
print(f"Addition:\n{A + B}\n")
show_shapes()
print(f"Subtraction:\n{A - B}\n")
show_shapes()
print(f"Element-wise multiplication:\n{A * B}\n")

# Matrix multiplication: A is (m x n), B must be (n x p) -> result (m x p)
show_shapes()
print(f"Matrix multiplication (A @ B):\n{A @ B}\n")

show_shapes()
print(f"Transpose of A:\n{A.T}\nTranspose of B:\n{B.T}\n")

# Determinant and inverse: need a SQUARE matrix; inverse also needs det != 0
show_shapes()
for name, M in (("A", A), ("B", B)):
    det = np.linalg.det(M)
    print(f"det({name}) = {det:.2f}")
    if np.isclose(det, 0):
        print(f"Inverse of {name}: not possible (singular matrix)\n")
    else:
        print(f"Inverse of {name}:\n{np.linalg.inv(M)}\n")

print("""Dimension requirements:
- Addition/Subtraction/Element-wise (*): both matrices must have the same shape.
- Matrix multiplication (@): columns of A must equal rows of B.
- Transpose: no restriction.
- Determinant/Inverse: matrix must be square; inverse also requires det != 0.""")
