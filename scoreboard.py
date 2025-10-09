from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("score.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.scores}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores}  High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.scores += 1
        self.update_score()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.scores>self.highscore:
            self.highscore=self.scores
            with open("score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.scores=0
        self.update_score()
