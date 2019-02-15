# Space Invaders
# Set up the screen
# Python 3.7.2 on Mac

import turtle
import os
import math
import random

# Set up the screen
os.chdir("sfx/")
os.system("afplay bgm.wav&")
os.chdir("..")

window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

os.chdir("img/")
window.bgpic("bg.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
os.chdir("..")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0) #0 is fastest
border_pen.color("#3DFF18")

border_pen.penup() #lift up the pen
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown() #put down the pen

for side in range(4):
    border_pen.fd(600) #forward 600 pixel
    border_pen.lt(90) #left turn 90 degree
border_pen.hideturtle()

# Draw the title
title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("#DD35F8")
title_pen.penup()
title_pen.setposition(0,300)
titlestring = "SPACE INVADER"
title_pen.write(titlestring, False, align="center", font=("Invasion 2028",32,"normal"))
title_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("#3DFF18")
score_pen.penup()
score_pen.setposition(-290,305)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Invasion 2028",20,"normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("purple")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90) #facing up
# 0(default)==right, 90==up, 180==left, 270==down

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:

    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    # y = random.randint(-200,0) #Testing Game over
    enemy.setposition(x,y)


enemyspeed = 5

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 30

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
        os.chdir("sfx/")
        os.system("afplay laser.wav&")
        os.chdir("..")
        bulletstate = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):# bool function normally named as isIt_true() "color_mark(darkred)""
    # Distance Formula: square root (X1-X2)^2 + (Y1-Y2)^2

    # math.sqrt stand for SQuare RooT
    # math.pow stand for POWer to
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))

    if distance < 25:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move the enemy down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1


        if enemy.xcor() < -280:
            # Move the enemy down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            os.chdir("sfx/")
            os.system("afplay explosion.wav&")
            os.chdir("..")
            #Reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #Update the score
            score += 100
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            #clear the previous socre
            score_pen.write(scorestring, False, align="left", font=("Invasion 2028",20,"normal"))

        # Check for a collision between the player and the enemy
        if (isCollision(player, enemy)) or (enemy.ycor() < -280):
            os.chdir("sfx/")
            os.system("killall afplay")
            os.system("afplay gameover.wav&")
            os.chdir("..")
            player.hideturtle()
            enemy.hideturtle()
            print("\n"+"-"*35)
            print("\n\n            Game Over!            \n\n")
            print("-"*35+"\n")
            window.bgcolor("black")
            window.title("Game Over")

            # Terminated
            exit()

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
