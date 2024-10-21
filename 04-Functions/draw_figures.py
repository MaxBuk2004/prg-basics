# draw_figures.py

import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

def draw_figures():
    # Draw square at two different locations
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    draw_square(pen, 100)

    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    draw_square(pen, 100)

    # Draw triangle at two different locations
    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    draw_triangle(pen, 100)

    pen.penup()
    pen.goto(100, -100)
    pen.pendown()
    draw_triangle(pen, 100)

    # Draw rectangle at two different locations
    pen.penup()
    pen.goto(-100, -200)
    pen.pendown()
    draw_rectangle(pen, 150, 75)

    pen.penup()
    pen.goto(100, -200)
    pen.pendown()
    draw_rectangle(pen, 150, 75)

# Execute drawing function
draw_figures()

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()