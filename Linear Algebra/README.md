# Linear Algebra Foundations for Machine Learning

This module contains from-scratch implementations of core linear algebra concepts used in machine learning.

---

## 🎯 Purpose

- Build mathematical intuition
- Implement core operations manually
- Connect linear algebra to ML systems

---

## 📚 Implemented Components

---

### 1️⃣ Dot Product

**Mathematical Definition**

For two vectors:

u = (u₁, u₂, ..., uₙ)  
v = (v₁, v₂, ..., vₙ)

The dot product is:

u · v = Σ (uᵢ vᵢ)

**Why It Matters**

- Measures similarity between vectors
- Core operation in matrix multiplication
- Used in neural network computations

**Implementation**

`dot(matrix1, matrix2, r, c)`

---

### 2️⃣ Matrix Multiplication

**Mathematical Definition**

If:

- Matrix A has shape (m × n)
- Matrix B has shape (n × p)

Then:

- The product C = A × B has shape (m × p)

Each element is computed as:

C[i][j] = dot(row_i_of_A, column_j_of_B)

**Why It Matters**

- Core of neural network layers
- Used in linear transformations
- Foundation of most ML algorithms

**Implementation**

`dot_matrix(matrix1, matrix2)`

---

## 🧪 Validation

All implementations are verified against NumPy:

```python
assert np.allclose(dot_matrix(A, B), A @ B)
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
