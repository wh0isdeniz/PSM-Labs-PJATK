import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
alpha_deg = 30  # incline angle in degrees
alpha = np.radians(alpha_deg)  # convert to radians

# Object definitions: sphere and disk
objects = {
    "sphere": {
        "mass": 1.0,   # kg
        "radius": 0.1, # m
        "inertia_factor": 2/5
    },
    "disk": {
        "mass": 1.0,   # kg
        "radius": 0.1, # m
        "inertia_factor": 1/2
    }
}

# Simulation parameters
dt = 0.01  # time step (s)
T = 2.0    # total simulation time (s)
N = int(T / dt)
time = np.linspace(0, T, N)

# Midpoint method simulation function with energy
def simulate_rolling_object_with_energy(mass, radius, inertia_factor):
    I = inertia_factor * mass * radius**2
    a = (g * np.sin(alpha)) / (1 + (I / (mass * radius**2)))

    s = np.zeros(N)
    v = np.zeros(N)
    beta = np.zeros(N)
    omega = np.zeros(N)

    PE = np.zeros(N)
    KE = np.zeros(N)
    E_total = np.zeros(N)

    for i in range(N - 1):
        # Midpoint estimates
        v_half = v[i] + 0.5 * dt * a
        s_half = s[i] + 0.5 * dt * v[i]

        omega_half = omega[i] + 0.5 * dt * (a / radius)
        beta_half = beta[i] + 0.5 * dt * omega[i]

        # Full step updates
        v[i+1] = v[i] + dt * a
        s[i+1] = s[i] + dt * v_half

        omega[i+1] = omega[i] + dt * (a / radius)
        beta[i+1] = beta[i] + dt * omega_half

        # Energy calculations
        height = s[i+1] * np.sin(alpha)
        PE[i+1] = mass * g * height
        KE_linear = 0.5 * mass * v[i+1]**2
        KE_rot = 0.5 * I * omega[i+1]**2
        KE[i+1] = KE_linear + KE_rot
        E_total[i+1] = PE[i+1] + KE[i+1]

    return s, v, beta, omega, PE, KE, E_total

# Running simulations
results = {}
for name, props in objects.items():
    s, v, beta, omega, PE, KE, E = simulate_rolling_object_with_energy(
        props["mass"], props["radius"], props["inertia_factor"]
    )
    results[name] = {
        "s": s, "v": v, "beta": beta, "omega": omega,
        "PE": PE, "KE": KE, "E": E
    }

# Plot center of mass position
plt.figure(figsize=(10, 4))
for name in results:
    plt.plot(time, results[name]["s"], label=f'{name} position')
plt.title("Center of Mass Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot rotation angle
plt.figure(figsize=(10, 4))
for name in results:
    plt.plot(time, results[name]["beta"], label=f'{name} rotation angle')
plt.title("Rotation Angle vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Rotation Angle (rad)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot energy graphs
for name in results:
    plt.figure(figsize=(10, 5))
    plt.plot(time, results[name]["PE"], label="Potential Energy")
    plt.plot(time, results[name]["KE"], label="Kinetic Energy")
    plt.plot(time, results[name]["E"], label="Total Energy", linestyle='--')
    plt.title(f"Energy vs Time for {name}")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
