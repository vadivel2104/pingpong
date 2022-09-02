from turtle import Turtle, Screen
SCREEN = Screen()


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle(0, 0)
        self.new_y = 0
        self.move(up="Up", down="Down")

    def create_paddle(self, x_cor, y_cor):
        self.penup()
        self.goto(x_cor, y_cor)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)

    def move(self, up="Up", down="Down"):
        SCREEN.listen()
        SCREEN.onkey(self.go_up, up)
        SCREEN.onkey(self.go_down, down)
