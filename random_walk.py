from turtle import Turtle
import random

direction = [0,90,270,360]
colors = ["red", "orange", "green", "purple", "pink", "brown", "black", "cyan", "magenta"]

tim = Turtle()
tim.speed(30)
tim.pensize(15)

for num in range(200):
    tim.forward(30)
    tim.left(random.choice(direction))
    tim.color(random.choice(colors))

