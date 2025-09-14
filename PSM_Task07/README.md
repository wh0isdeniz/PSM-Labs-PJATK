# 2D Heat Distribution in a Plate (Laplace Equation)

This project solves the **steady-state heat conduction problem** in a square plate using the **finite difference method**.  
The plate has fixed temperatures on each boundary, and the interior temperature distribution is computed by solving a large linear system.

## Problem Setup
- Square grid: 41 × 41 points (including boundaries)
- Boundary conditions:
  - **Top**: 200 °C
  - **Bottom**: -300 °C
  - **Left**: -200 °C
  - **Right**: 300 °C
- Governing equation: **Laplace equation**  
  \[
  \nabla^2 T = 0
  \]
  solved with Dirichlet boundary conditions.

## Method
- Finite difference discretization of Laplace’s equation.
- Sparse matrix representation (`scipy.sparse.lil_matrix`) for efficiency.
- Linear system \( A \cdot x = b \) solved with `spsolve`.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- SciPy

Install dependencies:
```bash
pip install numpy matplotlib scipy
