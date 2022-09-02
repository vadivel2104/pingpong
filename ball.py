from turtle import Turtle
import random as rn


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def ball_move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def ball_rebounce_wall(self):
        self.ymove *= -1

    def ball_rebounce_paddle(self):
        self.xmove *= -1

    def ball_refresh(self):
        self.goto(0, 0)
        self.xmove *= -1
