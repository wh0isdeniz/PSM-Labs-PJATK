import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81        # Gravity (m/s^2)
r = 1.0         # Pendulum length (m)
m = 1.0         # Mass (kg)
dt = 0.01       # Time step (s)
T = 10          # Total simulation time (s)
steps = int(T / dt)

# Initial conditions
alpha0 = np.radians(30)  # 30 degrees to radians
omega0 = 0.0             # Initial angular velocity

# Improved Euler Method (Heun)
def improved_euler(alpha0, omega0, dt, steps):
    alphas = np.zeros(steps)
    omegas = np.zeros(steps)
    times = np.linspace(0, steps * dt, steps)
    alphas[0] = alpha0
    omegas[0] = omega0

    for i in range(steps - 1):
        a = alphas[i]
        w = omegas[i]
        da1 = w
        dw1 = -(g / r) * np.sin(a)
        a_temp = a + da1 * dt
        w_temp = w + dw1 * dt
        da2 = w_temp
        dw2 = -(g / r) * np.sin(a_temp)
        alphas[i + 1] = a + (dt / 2) * (da1 + da2)
        omegas[i + 1] = w + (dt / 2) * (dw1 + dw2)

    return times, alphas, omegas

# RK4 Method
def rk4(alpha0, omega0, dt, steps):
    alphas = np.zeros(steps)
    omegas = np.zeros(steps)
    times = np.linspace(0, steps * dt, steps)
    alphas[0] = alpha0
    omegas[0] = omega0

    for i in range(steps - 1):
        a = alphas[i]
        w = omegas[i]
        k1_a = w
        k1_w = -(g / r) * np.sin(a)
        k2_a = w + 0.5 * dt * k1_w
        k2_w = -(g / r) * np.sin(a + 0.5 * dt * k1_a)
        k3_a = w + 0.5 * dt * k2_w
        k3_w = -(g / r) * np.sin(a + 0.5 * dt * k2_a)
        k4_a = w + dt * k3_w
        k4_w = -(g / r) * np.sin(a + dt * k3_a)
        alphas[i + 1] = a + (dt / 6) * (k1_a + 2 * k2_a + 2 * k3_a + k4_a)
        omegas[i + 1] = w + (dt / 6) * (k1_w + 2 * k2_w + 2 * k3_w + k4_w)

    return times, alphas, omegas

# Energy Calculation
def compute_energies(alphas, omegas):
    pe = m * g * r * (1 - np.cos(alphas))
    ke = 0.5 * m * (r * omegas) ** 2
    total = pe + ke
    return pe, ke, total

# Run simulations
t_euler, alpha_euler, omega_euler = improved_euler(alpha0, omega0, dt, steps)
t_rk4, alpha_rk4, omega_rk4 = rk4(alpha0, omega0, dt, steps)

# Compute energies
pe_euler, ke_euler, total_euler = compute_energies(alpha_euler, omega_euler)
pe_rk4, ke_rk4, total_rk4 = compute_energies(alpha_rk4, omega_rk4)

# Plotting
plt.figure(figsize=(14, 8))

# Angular displacement
plt.subplot(2, 2, 1)
plt.plot(t_euler, alpha_euler, label='Improved Euler')
plt.plot(t_rk4, alpha_rk4, label='RK4', linestyle='--')
plt.title("Angular Displacement vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()

# Total energy comparison
plt.subplot(2, 2, 2)
plt.plot(t_euler, total_euler, label='Improved Euler')
plt.plot(t_rk4, total_rk4, label='RK4', linestyle='--')
plt.title("Total Energy vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.legend()

# Energy components - Improved Euler
plt.subplot(2, 2, 3)
plt.plot(t_euler, pe_euler, label='Potential Energy')
plt.plot(t_euler, ke_euler, label='Kinetic Energy')
plt.plot(t_euler, total_euler, label='Total Energy', linestyle='--')
plt.title("Energy Components (Improved Euler)")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.legend()

# Energy components - RK4
plt.subplot(2, 2, 4)
plt.plot(t_rk4, pe_rk4, label='Potential Energy')
plt.plot(t_rk4, ke_rk4, label='Kinetic Energy')
plt.plot(t_rk4, total_rk4, label='Total Energy', linestyle='--')
plt.title("Energy Components (RK4)")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.legend()

plt.tight_layout()
plt.show()
