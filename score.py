from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score = 0
        self.position = (175, 280)
        self.player_score(self.position)

    def player_score(self, position):
        self.goto(position)
        self.write(f"Score: {self.update_score}", align="center", font=("courier", 10, "normal"))

    def score_update(self):
        self.clear()
        self.update_score += 1
        self.write(f"Score: {self.update_score}", align="center", font=("courier", 10, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 20, "normal"))
