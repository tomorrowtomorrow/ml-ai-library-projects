# Linear Algebra Foundations for Machine Learning

This module contains from-scratch implementations of core linear algebra concepts used in machine learning.

The goal of this section is not to replace NumPy, but to deeply understand the mathematical operations that power neural networks, optimization algorithms, and data transformations.

---

## 🎯 Purpose

- Build mathematical intuition
- Implement core operations manually
- Understand computational complexity
- Connect linear algebra to ML systems

---

## 📚 Implemented Components

### 1️⃣ Vector Operations
- Dot product
- Vector norms
- Basic vector utilities

### 2️⃣ Matrix Operations
- Row extraction
- Column extraction
- Matrix multiplication (manual implementation)
- Shape validation

### 3️⃣ Matrix Properties (Planned / In Progress)
- Transpose
- Determinant
- Inverse
- Rank
- Trace

### 4️⃣ Decompositions (Planned)
- LU Decomposition
- QR Decomposition
- Eigenvalues & Eigenvectors
- Singular Value Decomposition (SVD)

---

## 🧠 Mathematical Foundation

If:

- Matrix A has shape (m × n)
- Matrix B has shape (n × p)

Then:

- The product C = A × B has shape (m × p)

Each element is computed as:

C[i][j] = dot(row_i_of_A, column_j_of_B)

Understanding this operation is essential for:

- Linear transformations
- Neural network forward propagation
- Gradient computation
- Optimization methods

---

## ⚙️ Example Usage

```python
import numpy as np
from linear_algebra import dot_matrix

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = dot_matrix(A, B)
print(result)
