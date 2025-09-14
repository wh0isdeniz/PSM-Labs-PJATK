import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

# Grid size
n = 41  # 41x41 (including boundaries)

# inside the plate
inner_n = n - 2  # 39x39
N = inner_n * inner_n

# Boundary temperatures FROM lab_7 notes
top = 200
bottom = -300
left = -200
right = 300

# Create sparse matrix A and vector b for Ax = b
A = lil_matrix((N, N))
b = np.zeros(N)

# converting (i, j) in 2D to 1D index in x
def idx(i, j):
    return i * inner_n + j

# Building the equation system for each inner node
for i in range(inner_n):
    for j in range(inner_n):
        k = idx(i, j)
        A[k, k] = -4  # center point

        # Top neighbor
        if i > 0:
            A[k, idx(i - 1, j)] = 1
        else:
            b[k] -= top  # top boundary

        # Bottom neighbor
        if i < inner_n - 1:
            A[k, idx(i + 1, j)] = 1
        else:
            b[k] -= bottom  # bottom boundary

        # Left neighbor
        if j > 0:
            A[k, idx(i, j - 1)] = 1
        else:
            b[k] -= left  # left boundary

        # Right neighbor
        if j < inner_n - 1:
            A[k, idx(i, j + 1)] = 1
        else:
            b[k] -= right  # right boundary

x = spsolve(A.tocsr(), b)

# Reshaping the solution to 2D array
temperature = x.reshape((inner_n, inner_n))  # shape: (39, 39)

# Creating full temperature grid (41x41) including boundaries
full_temp = np.zeros((n, n))
full_temp[1:-1, 1:-1] = temperature

# Applying  boundary temperatures
full_temp[0, :] = top       # top row
full_temp[-1, :] = bottom   # bottom row
full_temp[:, 0] = left      # left column
full_temp[:, -1] = right    # right column

# Show temperature distribution as heatmap
plt.figure(figsize=(8, 6))
plt.imshow(full_temp, origin='lower', cmap='plasma')
plt.colorbar(label='Temperature (°C)')
plt.title('Temperature Distribution in the Plate')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
