# Vibrating String Simulation (Midpoint Method)

This project simulates the vibration of a **string with fixed ends**, modeled using the **wave equation**.  
The simulation applies the **Midpoint (Improved Euler) method** to approximate the motion of the string and track the system’s energy over time.

## Features
- Discretization of a string into points using finite differences
- Initial displacement set as a sinusoidal wave
- Fixed boundary conditions (string ends do not move)
- Numerical integration with the Midpoint method
- Computation of:
  - **Kinetic energy (Ek)**
  - **Potential energy (Ep)**
  - **Total energy (Et)**

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
