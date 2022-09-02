from turtle import Screen, Turtle
from paddle import Pong
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Pong()
l_paddle.create_paddle(-350, 0)
l_paddle.move("w", "s")
r_paddle = Pong()
r_paddle.create_paddle(350, 0)
r_paddle.move("Up", "Down")

ball = Ball()
r_score = Score()
l_score = Score()

r_score.player_score((175, 280))
l_score.player_score((-175, 280))

game_on = True

while game_on:
    time.sleep(0.09)
    screen.update()
    l_paddle.move()
    r_paddle.move()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_rebounce_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_rebounce_paddle()
    if ball.xcor() < -360:
        r_score.score_update()
        ball.ball_refresh()
    if ball.xcor() > 360:
        l_score.score_update()
        ball.ball_refresh()





















screen.exitonclick()
