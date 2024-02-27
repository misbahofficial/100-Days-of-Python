import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.speed('fastest')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

def draw_spiral(gap):
    for _ in range(int(360 / gap)):
        t.color(random_color())  # Set random color
        t.circle(100)  # Draw the circle
        t.setheading(t.heading() + gap)

draw_spiral(5)

screen = Screen()
screen.exitonclick()
