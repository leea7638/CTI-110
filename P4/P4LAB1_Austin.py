# CTI 110
# P4LAB1
# Austin Lee
# 10/06/2026

# set up your turtle
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("navyblue") # change this if you want

t = turtle.Turtle() # variable "t" now holds our turtle
# Set these to your preference
t.color("green")
t.shape("square") # turtle, square, circle, triangle...
t.pencolor("white")
t.fillcolor("orange")
t.pensize(3)

# Draw with it. (your code here)
sides = 4
angle = 360 / sides
length = 100
# example 1 - while loop
with t.fill():
    while sides > 0:
        t.forward(length)
        t.right(angle)
        sides = sides - 1
"""
# example 2 - for loop
t.teleport(-200, 0)
sides = 4
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()
"""
# put a roof on the house?
sides = 3
t.pencolor("black")
t.fillcolor("firebrick")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

# put a star in the sky
t.penup()
t.goto(200, 180)
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

# End - Keep window open
turtle.done()