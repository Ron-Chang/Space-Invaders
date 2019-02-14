# Space Invaders
# Set up the screen
# Python 3.7.2 on Mac

import turtle
import os

# Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0) #0 is fastest
border_pen.color("white")

border_pen.penup() #lift up the pen
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown() #put down the pen

for side in range(4):
    border_pen.fd(600) #forward 600 pixel
    border_pen.lt(90) #left turn 90 degree
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("purple")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90) #facing up
# 0(default)==right, 90==up, 180==left, 270==down







delay = input("Press enter to finish.")

