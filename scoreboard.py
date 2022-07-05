from turtle import Turtle
FONT = ("Courier", 19, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"Level ={self.score} ", move=False, align="left", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level = {self.score} ", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over, You were hit by a car", move=False, align="center", font=FONT)

