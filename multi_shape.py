from turtle import Turtle
import random

tim = Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta"]


def shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for n in range(3,11):
    tim.color(random.choice(colors))
    shape(int(n))