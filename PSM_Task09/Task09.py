import turtle
import math

def apply_rules(word):
    """Apply the L-system rules to the current word."""
    new_word = ""
    for char in word:
        if char == 'X':
            new_word += 'F+[[X]-X]-F[-FX]+X'
        elif char == 'F':
            new_word += 'FF'
        else:
            new_word += char
    return new_word

def draw_plant(t, word, angle, length):
    """Draw the plant using turtle graphics."""
    stack = []  # Stack to store positions and angles
    
    for char in word:
        if char == 'F':
            t.forward(length)
        elif char == '+':
            t.right(angle)
        elif char == '-':
            t.left(angle)
        elif char == '[':
            stack.append((t.pos(), t.heading()))
        elif char == ']':
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

def main():
    # Initialize turtle
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    
    angle = 25
    length = 5
    iterations = 5  # Number of iterations
    
    # Initial word
    word = 'X'
    
    for _ in range(iterations):
        word = apply_rules(word)
    
    # Draw the plant
    draw_plant(t, word, angle, length)
    
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main() 