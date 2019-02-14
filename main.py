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

playerspeed = 15

# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemy.setheading(270)

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.shapesize(0.15,0.5)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"







# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate

    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x, y)
        bullet.showturtle()

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x +=enemyspeed
    enemy.setx(x)

    # Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

# delay = input("Press enter to finish.")
