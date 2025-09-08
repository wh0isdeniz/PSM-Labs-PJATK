/* PSM Project 1 : Taylor series
 Student : Deniz Erdem Özkan
 */

package org.example;

import java.util.Scanner;

public class TaylorSeriesSin {

    // Calculating the Factorial
    public static long factorial(int num) {
        if (num == 0 || num == 1) return 1;
        long fact = 1;
        for (int i = 2; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }

    // Method to normalize the angle (in order to keep it between -π and π)
    public static double normalizeAngle(double x) {
        x = x % (2 * Math.PI);
        if (x > Math.PI) {
            x -= 2 * Math.PI;
        } else if (x < -Math.PI) {
            x += 2 * Math.PI;
        }
        return x;
    }

    // Method to compute sin(x) using Taylor series
    public static double sinTaylorSeries(double x, int terms) {
        x = normalizeAngle(x); // Normalize the angle
        double sinValue = x;
        double term = x; // First term is x itself
        int sign = -1;

        for (int n = 1; n < terms; n++) {
            term *= x * x / ((2 * n) * (2 * n + 1)); // Using previous term to calculate next one
            sinValue += sign * term;
            sign *= -1;
        }
        return sinValue;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // User input for angle unit
        int choice;
        do {
            System.out.println("Select angle unit: \n1 - Radians\n2 - Degrees");
            while (!scanner.hasNextInt()) {
                System.out.println("Unexpected invalid input! Please enter only  1 or 2.");
                scanner.next(); // Discarding invalid input
            }
            choice = scanner.nextInt();
        } while (choice != 1 && choice != 2);

        System.out.print("Enter the angle value: ");
        while (!scanner.hasNextDouble()) {
            System.out.println("Invalid unexpcted input! Please enter a valid number.");
            scanner.next(); // Discard invalid input
        }
        double x = scanner.nextDouble();

        // Convert degrees to radians...
        if (choice == 2) {
            x = Math.toRadians(x);
        }

        // Set number of terms for accuracy
        int terms = 10;

        // Compute Taylor series approximation
        double result = sinTaylorSeries(x, terms);
        double mathSin = Math.sin(x);
        double error = Math.abs(result - mathSin);

        // Printing the results
        System.out.println("Sin(" + x + ") calculated by using Taylor series = " + result);
        System.out.println("Math.sin(" + x + ") = " + mathSin);
        System.out.println("Absolute error: " + error); // Basically the difference between results

        scanner.close();
    }
}
