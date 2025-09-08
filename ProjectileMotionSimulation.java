package org.example;

class Vector2D { // A class representing a 2D vector (used for position and velocity)
    public double x, y;

    public Vector2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Adding another vector to this vector
    public Vector2D add(Vector2D other) {
        return new Vector2D(this.x + other.x, this.y + other.y);
    }

    // Multipliying this vector by a scalar value
    public Vector2D multiply(double scalar) {
        return new Vector2D(this.x * scalar, this.y * scalar);
    }

    // Returns the magnitude (length) of the vector
    public double magnitude() {
        return Math.sqrt(x * x + y * y);
    }
}

abstract class Simulation {
    protected double mass, gravity, dragCoeff, dt;
    protected int steps;
    protected Vector2D position, velocity;

    public Simulation(double mass, double gravity, double dragCoeff, double dt, int steps, Vector2D position, Vector2D velocity) {
        this.mass = mass;
        this.gravity = gravity;
        this.dragCoeff = dragCoeff;
        this.dt = dt;
        this.steps = steps;
        this.position = position;
        this.velocity = velocity;
    }

    protected abstract void step();

    // Runs the simulation for the given number of steps or until the projectile hits the ground
    public void run() {
        for (int i = 0; i < steps; i++) {
            step();

            System.out.printf("Step %d: Position(%.2f, %.2f) ---- Velocity(%.2f, %.2f)\n",
                    i, position.x, position.y, velocity.x, velocity.y);

            // Stop simulation if projectile hits the ground
            if (position.y < 0) {
                double tImpact = -position.y / velocity.y;
                double xImpact = position.x + velocity.x * tImpact;
                System.out.printf("Projectile hit the ground at (%.2f, 0)\n", xImpact);
                break;
            }
        }
    }
}
// Implements Euler's Method for the simulation
class EulerMethod extends Simulation {
    public EulerMethod(double mass, double gravity, double dragCoeff, double dt, int steps, Vector2D position, Vector2D velocity) {
        super(mass, gravity, dragCoeff, dt, steps, position, velocity);
    }

    @Override
    protected void step() {
        double speed = velocity.magnitude();
        double dragForce = (dragCoeff * speed * speed) / mass;
        double ax = -dragForce * (velocity.x / speed);
        double ay = gravity - (dragForce * (velocity.y / speed));
        Vector2D acceleration = new Vector2D(ax, ay);

        velocity = velocity.add(acceleration.multiply(dt));
        position = position.add(velocity.multiply(dt));
    }
}

// Implements Midpoint Method (improved Euler's Method)
class MidpointMethod extends Simulation {
    public MidpointMethod(double mass, double gravity, double dragCoeff, double dt, int steps, Vector2D position, Vector2D velocity) {
        super(mass, gravity, dragCoeff, dt, steps, position, velocity);
    }

    @Override
    protected void step() {
        double speed = velocity.magnitude();
        double dragForce = (dragCoeff * speed * speed) / mass;
        double ax1 = -dragForce * (velocity.x / speed);
        double ay1 = gravity - (dragForce * (velocity.y / speed));
        Vector2D acceleration1 = new Vector2D(ax1, ay1);

        Vector2D velocityHalfStep = velocity.add(acceleration1.multiply(dt / 2));

        double speedHalf = velocityHalfStep.magnitude();
        double dragForceHalf = (dragCoeff * speedHalf * speedHalf) / mass;
        double ax2 = -dragForceHalf * (velocityHalfStep.x / speedHalf);
        double ay2 = gravity - (dragForceHalf * (velocityHalfStep.y / speedHalf));
        Vector2D acceleration2 = new Vector2D(ax2, ay2);

        // Update velocity and position
        velocity = velocity.add(acceleration2.multiply(dt));
        position = position.add(velocity.multiply(dt));
    }
}
// Main class to run the simulation
public class ProjectileMotionSimulation {
    public static void main(String[] args) {
        double mass = 1.0;
        double gravity = 9.81;
        double dragCoeff = 0.1;
        double dt = 0.01;
        int steps = 1000;

        // Running the simulation using Euler's method
        System.out.println("Results of Euler Method:");
        new EulerMethod(mass, gravity, dragCoeff, dt, steps, new Vector2D(0, 0), new Vector2D(10, 10)).run();

        // Running the simulation using Midpoint method
        System.out.println("\nResults of Midpoint Method:");
        new MidpointMethod(mass, gravity, dragCoeff, dt, steps, new Vector2D(0, 0), new Vector2D(10, 10)).run();
    }
}
