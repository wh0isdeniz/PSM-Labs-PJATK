# Taylor Series Sine Approximation

This project was created as the **1st assignment** for the *Foundations of Computer Simulations (PSM)* course at **PJATK**.  

## Project Description
A Java program that approximates `sin(x)` using the Taylor series expansion.  
The program:  
- Allows the user to choose between **radians** or **degrees** as the input unit.  
- Normalizes the angle to the range \([-π, π]\).  
- Uses **10 terms** of the Taylor series for the approximation.  
- Compares the result with Java’s built-in `Math.sin(x)` function.  
- Prints the absolute error between the two values.  

This demonstrates how numerical methods can approximate mathematical functions and how accuracy improves with more terms in the series.

## Usage
```bash
javac TaylorSeriesSin.java
java TaylorSeriesSin
