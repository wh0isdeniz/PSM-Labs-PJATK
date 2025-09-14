# Rolling Objects Simulation (Midpoint Method)

This project simulates the motion of a **solid sphere** and a **solid disk** rolling down an inclined plane without slipping.  
The simulation uses the **Midpoint numerical integration method** to calculate linear and rotational motion, as well as energy transformations.

## Features
- Inclined plane with adjustable angle (default: 30°)
- Two rolling objects:
  - Sphere (moment of inertia factor = 2/5)
  - Disk (moment of inertia factor = 1/2)
- Calculates and plots:
  - Center of mass position vs time
  - Rotation angle vs time
  - Potential, kinetic, and total energy vs time
- Verifies conservation of energy

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies with:
```bash
pip install numpy matplotlib
