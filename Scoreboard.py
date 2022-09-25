from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()

    def game_over(self):
        self.goto(0, 20)
        self.clear()
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -20)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))