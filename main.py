import turtle
import random

# Functions: a group of related statements that perform a specific task
# functions help us breakdown our program into sections
# DRY: Don't Repeat Yourself
# Formula
# def functionName(parameters):
#     BODY
#     optional 'return' statement
blue = turtle.Turtle()
red = turtle.Turtle()
yellow = turtle.Turtle()
gray = turtle.Turtle()
gold = turtle.Turtle() 
def drawTrack(length):
  cameraMan = turtle.Turtle()
  cameraMan.shape("triangle")
  cameraMan.speed(0)
  cameraMan.penup()
  cameraMan.goto(-175, 140)

  # Race Track
  for i in range(length):
    cameraMan.write(" ")
    # Drawing the Line
    cameraMan.right(90)
    cameraMan.forward(250)
    cameraMan.right(180)
    cameraMan.forward(250)
    # Return
    cameraMan.penup()
    cameraMan.right(90)
    # Number
    cameraMan.right(90)
    cameraMan.write(i)
    cameraMan.left(90)
    cameraMan.pendown()
    # Return 2
    cameraMan.penup()
    cameraMan.backward(5)
    cameraMan.forward(35) 
    cameraMan.pendown()
  cameraMan.hideturtle()

def createTurtles():
  blue.shape("turtle")
  blue.penup()
  blue.goto(-200, 100)
  blue.color("blue")

  red.shape("turtle")
  red.penup()
  red.goto(-200, 60)
  red.color("red")

  yellow.shape("turtle")
  yellow.penup()
  yellow.goto(-200, 20)
  yellow.color("yellow")

  gray.shape("turtle")
  gray.penup()
  gray.goto(-200, -20)
  gray.color("gray")

  gold.shape("turtle")
  gold.penup()
  gold.goto(-200, -60)
  gold.color("gray")

  blue.penup()
  yellow.penup()
  red.penup()
  gray.penup()
  gold.penup()

def startrace():
  blue.pendown()
  yellow.pendown()
  red.pendown()
  gray.pendown()
  gold.pendown()

  while(True):
    blue.forward(random.randint(1,15))
    red.forward(random.randint(1,15))
    yellow.forward(random.randint(1,15))
    gray.forward(random.randint(1,15))
    gold.forward(random.randint(1,15))

drawTrack(17)
createTurtles()
startrace()