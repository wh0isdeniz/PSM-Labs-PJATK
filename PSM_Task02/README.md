# Projectile Motion Simulation

This project was created as part of the *Foundations of Computer Simulations (PSM)* course at **PJATK**.  
It demonstrates the numerical simulation of projectile motion with air resistance using two different methods.

## Project Description
A Java program that simulates the trajectory of a projectile under gravity and drag force.  
The simulation is implemented with two numerical integration techniques:  
- **Euler’s Method** – a simple step-by-step approximation.  
- **Midpoint Method (Improved Euler’s Method)** – a more accurate variation.  

The program prints the projectile’s position and velocity at each step and detects when it hits the ground.

## Usage
```bash
javac ProjectileMotionSimulation.java
java ProjectileMotionSimulation
