
# Part 1: Drawing Basic Shapes

import turtle
import random


# Function to draw a square
def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)


# Function to draw a circle
def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


# Function to draw a regular polygon
def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


# Part 2: Creating Composite Shapes

# Function to draw a pumpkin
def draw_pumpkin(t, x, y, radius):
    """Draws an orange pumpkin with a green stem."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    # Draw the orange pumpkin
    t.color("orange")
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Draw the stem at the top of the pumpkin
    t.penup()
    t.goto(x, y + radius * 2)
    t.setheading(90)
    t.pendown()

    t.color("green")
    t.fillcolor("green")
    t.begin_fill()
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.right(90)
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.end_fill()


# Function to draw a triangular eye
def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()


# Function to draw a jagged mouth
def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using connected lines."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color("yellow")
    t.fillcolor("yellow")
    t.begin_fill()

    # Draw the top edge
    t.forward(width)

    # Draw the zigzag bottom edge
    for _ in range(5):
        t.right(120)
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)

    # Close the mouth shape
    t.goto(x, y)
    t.end_fill()


# Test the pumpkin functions
# These calls are examples; the final scene is drawn below.


# Part 3: Let the Stars Shine for You

# Function to draw a star
def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color("white")
    t.fillcolor("white")
    t.begin_fill()

    for _ in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()


# Function to draw random stars
def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-280, 280)
        y = random.randint(150, 270)
        size = random.randint(10, 20)
        draw_star(t, x, y, size)


# Set up the turtle screen BEFORE creating the turtle
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
screen.title("Halloween Night")


# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)
t.hideturtle()

# Clear the screen
t.clear()


# Part 4: Putting Everything Together

# Draw the left jack-o-lantern
draw_pumpkin(t, -150, -250, 50)
draw_eye(t, -170, -180, 20)
draw_eye(t, -130, -180, 20)
draw_mouth(t, -180, -215, 60)

# Draw the middle jack-o-lantern
draw_pumpkin(t, 0, -250, 40)
draw_eye(t, -15, -190, 18)
draw_eye(t, 15, -190, 18)
draw_mouth(t, -24, -215, 48)

# Draw the right jack-o-lantern
draw_pumpkin(t, 150, -250, 50)
draw_eye(t, 130, -180, 20)
draw_eye(t, 170, -180, 20)
draw_mouth(t, 120, -215, 60)

# Draw the night sky
draw_sky(t, 30)


# Close the turtle graphics window when clicked
turtle.exitonclick()