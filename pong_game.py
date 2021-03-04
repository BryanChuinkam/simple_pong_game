# simple Pong in Python 3 for Beginners
# TODO Add sound effects from https://freesound.org/

import turtle
import os

wn = turtle.Screen() 				# creating a window
wn.title("Pong for Caleb")
wn.bgcolor("black")
wn.setup(width=800, height=600)		# size of window
wn.tracer(0)						# stops window from updating. Hence speeding up game
initial_speed = 0.025

# prompt players for their name
player_one = turtle.textinput("Enter First Player name", "Player one: ")
player_two = turtle.textinput("Enter Second Player name", "Player two: ")

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)					# speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)					# speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)					# speed of animation NOT speed of ball
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = initial_speed
ball.dy = initial_speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0  {}: 0".format(player_one, player_two), align="center", font=("Courier", 24, "normal"))

# Functions


def paddle_a_up():
	""" moves paddle_a"""
	y = paddle_a.ycor()			# get y coordinates of paddle_a
	y += 20						# move it up by 20 pixels
	paddle_a.sety(y)			# set new y coordinate


def paddle_a_down():
	""" moves paddle_a"""
	y = paddle_a.ycor()			# get y coordinates of paddle_a
	y += -20						# move it down by 20 pixels
	paddle_a.sety(y)			# set new y coordinate


def paddle_b_up():
	""" moves paddle_b"""
	y = paddle_b.ycor()			# get y coordinates of paddle_b
	y += 20						# move it up by 20 pixels
	paddle_b.sety(y)			# set new y coordinate


def paddle_b_down():
	""" moves paddle_b"""
	y = paddle_b.ycor()			# get y coordinates of paddle_b
	y += -20					# move it down by 20 pixels
	paddle_b.sety(y)			# set new y coordinate

# keyboard binding


wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

# main game loop

while True:
	wn.update()

	# move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 		# reverses direction
		# os.system("aplay bounce.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy*= -1 		# reverses direction
		# os.system("aplay bounce.wav&")

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx = initial_speed  # reset speed after a player scores
		score_a += 1
		pen.clear()
		pen.write("{}: {}  {}: {}".format(player_one, score_a, player_two, score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx = initial_speed  # reset speed after a player scores
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("{}: {}  {}: {}".format(player_one, score_a, player_two, score_b), align="center", font=("Courier", 24, "normal"))

	# paddle and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
		ball.setx(340)
		ball.dx *= -1
		ball.dx -= 0.025  # speed it up
		# os.system("aplay bounce.wav&")

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
		ball.setx(-340)
		ball.dx *= -1
		ball.dx += 0.025  # speed it up
		# os.system("aplay bounce.wav&")