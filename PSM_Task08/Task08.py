import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 10
B = 25
C = 8 / 3
dt = 0.03
t0 = 0
tf = 100  # final time
n = int((tf - t0) / dt)  # number of steps

# Initial conditions
x0, y0, z0 = 1, 1, 1


# Lorenz system equations
def lorenz(x, y, z):
    dxdt = A * (y - x)
    dydt = -x * z + B * x - y
    dzdt = x * y - C * z
    return dxdt, dydt, dzdt


# Euler method
def euler_method():
    x, y, z = np.zeros(n), np.zeros(n), np.zeros(n)
    x[0], y[0], z[0] = x0, y0, z0

    for i in range(n - 1):
        dxdt, dydt, dzdt = lorenz(x[i], y[i], z[i])
        x[i + 1] = x[i] + dt * dxdt
        y[i + 1] = y[i] + dt * dydt
        z[i + 1] = z[i] + dt * dzdt

    return x, y, z


# Midpoint method
def midpoint_method():
    x, y, z = np.zeros(n), np.zeros(n), np.zeros(n)
    x[0], y[0], z[0] = x0, y0, z0

    for i in range(n - 1):
        # First step (Euler half-step)
        kx1, ky1, kz1 = lorenz(x[i], y[i], z[i])
        x_mid = x[i] + 0.5 * dt * kx1
        y_mid = y[i] + 0.5 * dt * ky1
        z_mid = z[i] + 0.5 * dt * kz1

        # Second step (using midpoint derivatives)
        kx2, ky2, kz2 = lorenz(x_mid, y_mid, z_mid)
        x[i + 1] = x[i] + dt * kx2
        y[i + 1] = y[i] + dt * ky2
        z[i + 1] = z[i] + dt * kz2

    return x, y, z


# RK4 method
def rk4_method():
    x, y, z = np.zeros(n), np.zeros(n), np.zeros(n)
    x[0], y[0], z[0] = x0, y0, z0

    for i in range(n - 1):
        # Step 1
        kx1, ky1, kz1 = lorenz(x[i], y[i], z[i])

        # Step 2
        kx2, ky2, kz2 = lorenz(x[i] + 0.5 * dt * kx1, y[i] + 0.5 * dt * ky1, z[i] + 0.5 * dt * kz1)

        # Step 3
        kx3, ky3, kz3 = lorenz(x[i] + 0.5 * dt * kx2, y[i] + 0.5 * dt * ky2, z[i] + 0.5 * dt * kz2)

        # Step 4
        kx4, ky4, kz4 = lorenz(x[i] + dt * kx3, y[i] + dt * ky3, z[i] + dt * kz3)

        # Update
        x[i + 1] = x[i] + (dt / 6) * (kx1 + 2 * kx2 + 2 * kx3 + kx4)
        y[i + 1] = y[i] + (dt / 6) * (ky1 + 2 * ky2 + 2 * ky3 + ky4)
        z[i + 1] = z[i] + (dt / 6) * (kz1 + 2 * kz2 + 2 * kz3 + kz4)

    return x, y, z


x_e, y_e, z_e = euler_method()
x_m, y_m, z_m = midpoint_method()
x_r, y_r, z_r = rk4_method()

# Plot z vs x for all methods
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x_e, z_e, 'b', linewidth=0.5)
plt.title('Euler Method: z vs x')
plt.xlabel('x')
plt.ylabel('z')

plt.subplot(3, 1, 2)
plt.plot(x_m, z_m, 'r', linewidth=0.5)
plt.title('Midpoint Method: z vs x')
plt.xlabel('x')
plt.ylabel('z')

plt.subplot(3, 1, 3)
plt.plot(x_r, z_r, 'g', linewidth=0.5)
plt.title('RK4 Method: z vs x')
plt.xlabel('x')
plt.ylabel('z')

plt.tight_layout()
plt.show()