from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down,'s')

game_ison = True
speed_up = 1
while game_ison:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if not (-280 <= ball.ycor() <= 280):
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        speed_up += 1
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.refresh()
        score.lpoint()
    
    if ball.xcor() < -380:
        ball.refresh()
        score.rpoint()

screen.exitonclick()