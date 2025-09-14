# Sun–Earth–Moon System Simulation (Midpoint Method)

This project simulates the motion of the **Earth** around the **Sun**, and the **Moon** around the Earth (while also being influenced by the Sun’s gravity).  
The simulation uses the **Improved Euler (Midpoint) method** to numerically integrate the equations of motion.

## Features
- Gravitational interactions:
  - Sun–Earth
  - Sun–Moon
  - Earth–Moon
- Numerical integration using the Midpoint method
- One year of simulation with a 1-hour time step
- Visualization of:
  - Earth’s nearly circular orbit around the Sun
  - Moon’s trajectory around the Earth (and relative to the Sun)

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
