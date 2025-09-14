import numpy as np
import matplotlib.pyplot as plt

# Constants
L = np.pi         # Length of the string
N = 10            # Number of discrete points
c = 1             # Wave propagation speed
dx = L / N        # Spatial step
dt = 0.01         # Time step
T = 10            # Total simulation time
steps = int(T / dt)

# Spatial positions along the string
x = np.linspace(0, L, N + 1)

# Initial displacement (sinusoidal shape)
y = np.sin(x)
y[0] = 0
y[-1] = 0

# Initial velocity
v = np.zeros(N + 1)

# Function to compute acceleration using finite difference
def compute_acceleration(y, dx):
    a = np.zeros_like(y)
    for i in range(1, len(y) - 1):
        a[i] = (y[i - 1] - 2 * y[i] + y[i + 1]) / dx**2
    return a

# Lists to store energy values over time
potential_energy = []
kinetic_energy = []
total_energy = []

# Time evolution loop using the Midpoint Method
for step in range(steps):
    # Compute acceleration at current time
    a = compute_acceleration(y, dx)

    # Midpoint prediction
    v_half = v + 0.5 * dt * a
    y_half = y + 0.5 * dt * v

    # Acceleration at midpoint
    a_half = compute_acceleration(y_half, dx)

    # Full-step update
    v += dt * a_half
    y += dt * v_half

    # Apply boundary conditions (fixed ends)
    y[0] = 0
    y[-1] = 0
    v[0] = 0
    v[-1] = 0

    # Compute energies
    Ek = 0.5 * dx * np.sum(v**2)
    Ep = 0.5 * np.sum(((y[1:] - y[:-1])**2) / dx)
    Et = Ek + Ep

    kinetic_energy.append(Ek)
    potential_energy.append(Ep)
    total_energy.append(Et)

# Time array for plotting
time = np.linspace(0, T, steps)

# Plot energies over time
plt.figure(figsize=(10, 6))
plt.plot(time, kinetic_energy, label='Kinetic Energy (Ek)')
plt.plot(time, potential_energy, label='Potential Energy (Ep)')
plt.plot(time, total_energy, label='Total Energy (Et)', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy of the Vibrating String Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
