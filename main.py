import turtle

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")
cameraMan.speed(0)

# Race Track
for i in range(16):
  cameraMan.write("")
  # Drawing the Line
  cameraMan.right(90)
  cameraMan.forward(100)
  cameraMan.right(180)
  cameraMan.forward(100)
  # Return
  cameraMan.penup()
  cameraMan.right(90)
  # Number
  cameraMan.penup()
  cameraMan.right(90)
  cameraMan.forward(5)
  cameraMan.write(i)
  cameraMan.left(90)
  cameraMan.pendown()
  # Return 2
  cameraMan.penup()
  cameraMan.backward(5)
  cameraMan.forward(20) 
  cameraMan.pendown()

  