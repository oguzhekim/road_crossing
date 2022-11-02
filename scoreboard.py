from turtle import Turtle
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.penup()
        self.goto(-290, 270)
        self.color("black")
        self.write(arg=f"Level: {self.level}", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(arg="GAME OVER", align="center", font=FONT)
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.refresh_score()
