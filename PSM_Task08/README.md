# Lorenz System Simulation (Euler, Midpoint, RK4)

This project simulates the **Lorenz system**, a set of nonlinear differential equations that exhibit **chaotic behavior**, using three different numerical integration methods:  
- Euler Method  
- Midpoint Method  
- Runge-Kutta 4 (RK4) Method  

The results are compared visually by plotting `z` vs `x`.

---

## Lorenz Equations
The system is defined as:

\[
\frac{dx}{dt} = A (y - x)
\]  
\[
\frac{dy}{dt} = -xz + Bx - y
\]  
\[
\frac{dz}{dt} = xy - Cz
\]

where:
- \( A = 10 \) (Prandtl number)  
- \( B = 25 \) (Rayleigh number)  
- \( C = \frac{8}{3} \) (geometric factor)

---

## Methods Implemented
1. **Euler Method** – simple, but less accurate for chaotic systems.  
2. **Midpoint Method** – a 2nd-order method, more stable.  
3. **Runge-Kutta 4 (RK4)** – a 4th-order method, very accurate.  

---

## Parameters
- Time step: `dt = 0.03`  
- Total time: `tf = 100`  
- Initial condition: `(x0, y0, z0) = (1, 1, 1)`  

---

## Requirements
- Python 3.x  
- NumPy  
- Matplotlib  

Install dependencies:
```bash
pip install numpy matplotlib
