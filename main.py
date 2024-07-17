import turtle
import random
score = 0
alive = True

sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

sd = turtle.Turtle()
sd.speed(0)
sd.color("blue")
sd.penup()
sd.hideturtle()
sd.goto(0, 200)
sd.write("Score: " + str(score), align="center", font=("Courier", 24, "normal"))

pad = turtle.Turtle()
pad.speed(0)
pad.shape("square")
pad.color("black")
pad.shapesize(stretch_wid=2, stretch_len=6)
pad.penup()
pad.goto(0,-250)

ball = turtle.Turtle()
ball.speed(20)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.dx = 0
ball.dy = -5
ball.goto(0,280)

def right():
  x = pad.xcor()
  x += 10
  pad.setx(x)
  
def left():
  x = pad.xcor()
  x -= 10
  pad.setx(x)

def restart():
  score = 0
  ball.goto(0,280)
  pad.goto(0,-250)
  alive = True
  
sc.listen()
sc.onkeypress(left, "a")
sc.onkeypress(right, "d")
sc.onkeypress(restart, "x")

while alive == True:
      sc.update()
      ball.setx(ball.xcor()+ball.dx)
      ball.sety(ball.ycor()+ball.dy)

      #distance = ball.xcor() - pad.xcor()
      #distance1 = ball.ycor() - pad.ycor()
      distance = ball.distance(pad.xcor(), pad.ycor())
      if distance < 60:
        x = random.randint(2,570)
        ball.goto(x,280)
        score += 1
        sd.clear()
        sd.write("Score: " + str(score), align="center", font=("Courier", 24, "normal"))

      if ball.ycor() < -300:
        x = random.randint(2,570)
        ball.goto(x,280)
        alive = False

else:
  display = turtle.Turtle()
  display.speed(0)
  display.color("blue")
  display.penup()
  display.hideturtle()
  display.goto(0,0)
  display.write("Game Over! Score: " + str(score), align="center", font=("Courier", 24, "normal"))


#MAKE IT SO BALL SPAWNS ON BOTH SIDE with + and - axis


	
