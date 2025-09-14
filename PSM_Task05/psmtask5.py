import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.6743e-11  # Gravitational constant [Nm^2/kg^2]
Ms = 1.989e30  # Mass of the Sun [kg]
Mz = 5.972e24  # Mass of the Earth [kg]
Mk = 7.347e22  # Mass of the Moon [kg]
R_ZS = 1.5e11  # Earth-Sun distance [m] (converted from km)
R_ZK = 3.844e8  # Earth-Moon distance [m] (converted from km)

# Time parameters
days = 365 
dt = 3600  # Time step in seconds (1 hour)
steps = int(days * 24 * 3600 / dt)  # Total number of steps

# Initial conditions
# Earth initial position (circular orbit assumption)
theta_earth_0 = 0
x_earth_0 = R_ZS * np.cos(theta_earth_0)
y_earth_0 = R_ZS * np.sin(theta_earth_0)

# Earth initial velocity (circular orbit velocity)
v_earth = np.sqrt(G * Ms / R_ZS)
vx_earth_0 = -v_earth * np.sin(theta_earth_0)
vy_earth_0 = v_earth * np.cos(theta_earth_0)

# Moon initial position relative to Earth (circular orbit assumption)
theta_moon_0 = 0
x_moon_rel_0 = R_ZK * np.cos(theta_moon_0)
y_moon_rel_0 = R_ZK * np.sin(theta_moon_0)

# Moon initial velocity relative to Earth (circular orbit velocity)
v_moon = np.sqrt(G * Mz / R_ZK)
vx_moon_rel_0 = -v_moon * np.sin(theta_moon_0)
vy_moon_rel_0 = v_moon * np.cos(theta_moon_0)

# Initialize arrays to store positions
x_earth = np.zeros(steps)
y_earth = np.zeros(steps)
x_moon = np.zeros(steps)
y_moon = np.zeros(steps)

# Set initial conditions
x_earth[0] = x_earth_0
y_earth[0] = y_earth_0
x_moon[0] = x_earth_0 + x_moon_rel_0
y_moon[0] = y_earth_0 + y_moon_rel_0

# Velocity arrays
vx_earth = np.zeros(steps)
vy_earth = np.zeros(steps)
vx_moon = np.zeros(steps)
vy_moon = np.zeros(steps)

vx_earth[0] = vx_earth_0
vy_earth[0] = vy_earth_0
vx_moon[0] = vx_earth_0 + vx_moon_rel_0
vy_moon[0] = vy_earth_0 + vy_moon_rel_0

# Improved Euler (Midpoint) method implementation
for i in range(steps - 1):
    # Current positions and velocities
    xe, ye = x_earth[i], y_earth[i]
    xm, ym = x_moon[i], y_moon[i]
    vxe, vye = vx_earth[i], vy_earth[i]
    vxm, vym = vx_moon[i], vy_moon[i]

    # Distance calculations
    r_es = np.sqrt(xe ** 2 + ye ** 2)  # Earth-Sun distance
    r_em = np.sqrt((xm - xe) ** 2 + (ym - ye) ** 2)  # Moon-Earth distance
    r_ms = np.sqrt(xm ** 2 + ym ** 2)  # Moon-Sun distance

    # Current accelerations
    # Earth acceleration due to Sun
    ax_earth = -G * Ms * xe / r_es ** 3
    ay_earth = -G * Ms * ye / r_es ** 3

    # Moon acceleration components
    # Due to Sun
    ax_moon_sun = -G * Ms * xm / r_ms ** 3
    ay_moon_sun = -G * Ms * ym / r_ms ** 3

    # Due to Earth
    ax_moon_earth = -G * Mz * (xm - xe) / r_em ** 3
    ay_moon_earth = -G * Mz * (ym - ye) / r_em ** 3

    # Total moon acceleration
    ax_moon = ax_moon_sun + ax_moon_earth
    ay_moon = ay_moon_sun + ay_moon_earth

    # Predictor step (Euler)
    xe_pred = xe + vxe * dt / 2
    ye_pred = ye + vye * dt / 2
    xm_pred = xm + vxm * dt / 2
    ym_pred = ym + vym * dt / 2

    vxe_pred = vxe + ax_earth * dt / 2
    vye_pred = vye + ay_earth * dt / 2
    vxm_pred = vxm + ax_moon * dt / 2
    vym_pred = vym + ay_moon * dt / 2

    # Recalculate distances at midpoint
    r_es_pred = np.sqrt(xe_pred ** 2 + ye_pred ** 2)
    r_em_pred = np.sqrt((xm_pred - xe_pred) ** 2 + (ym_pred - ye_pred) ** 2)
    r_ms_pred = np.sqrt(xm_pred ** 2 + ym_pred ** 2)

    # Recalculate accelerations at midpoint
    # Earth acceleration due to Sun at midpoint
    ax_earth_pred = -G * Ms * xe_pred / r_es_pred ** 3
    ay_earth_pred = -G * Ms * ye_pred / r_es_pred ** 3

    # Moon acceleration components at midpoint
    # Due to Sun
    ax_moon_sun_pred = -G * Ms * xm_pred / r_ms_pred ** 3
    ay_moon_sun_pred = -G * Ms * ym_pred / r_ms_pred ** 3

    # Due to Earth
    ax_moon_earth_pred = -G * Mz * (xm_pred - xe_pred) / r_em_pred ** 3
    ay_moon_earth_pred = -G * Mz * (ym_pred - ye_pred) / r_em_pred ** 3

    # Total moon acceleration at midpoint
    ax_moon_pred = ax_moon_sun_pred + ax_moon_earth_pred
    ay_moon_pred = ay_moon_sun_pred + ay_moon_earth_pred

    # Corrector step
    x_earth[i + 1] = xe + vxe_pred * dt
    y_earth[i + 1] = ye + vye_pred * dt
    x_moon[i + 1] = xm + vxm_pred * dt
    y_moon[i + 1] = ym + vym_pred * dt

    vx_earth[i + 1] = vxe + ax_earth_pred * dt
    vy_earth[i + 1] = vye + ay_earth_pred * dt
    vx_moon[i + 1] = vxm + ax_moon_pred * dt
    vy_moon[i + 1] = vym + ay_moon_pred * dt

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x_earth, y_earth, 'b', label="Earth's orbit")
plt.plot(x_moon, y_moon, 'r', label="Moon's trajectory", alpha=0.5)
plt.plot(0, 0, 'yo', markersize=10, label="Sun")  # Sun at origin

# Add some annotations
plt.plot(x_earth[0], y_earth[0], 'bo', label="Earth start")
plt.plot(x_moon[0], y_moon[0], 'ro', label="Moon start")

plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.title("Moon's Trajectory Relative to the Sun")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()