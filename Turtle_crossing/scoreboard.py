from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-220, 240)
        self.increase_level()

    def if_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align='center', font=FONT)



