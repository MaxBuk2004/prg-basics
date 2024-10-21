# figures.py

import turtle

def draw_square(pen, length):
    """Draw a square with the specified side length."""
    pen.speed(5)  # Set the speed of the turtle

    # Draw the square
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    """Draw an isosceles triangle with the specified side length."""
    pen.speed(5)  # Set the speed of the turtle

    # Draw the isosceles triangle
    for _ in range(2):
        pen.forward(length)
        pen.left(120)
    pen.forward(length)  # Complete the triangle

def draw_rectangle(pen, length_a, length_b):
    """Draw a rectangle with sides a and b."""
    pen.speed(5)  # Set the speed of the turtle

    # Draw the rectangle
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
