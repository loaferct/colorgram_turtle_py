import turtle as t
import random

colors = ["red", "orange", "green", "purple", "pink", "brown", "black", "cyan", "magenta"]

tim = t.Turtle()

tim.speed("fastest")

def circle(n):
    for i in range(int(360/n)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading()+n)

circle(5)
screen = t.Screen()
screen.exitonclick()