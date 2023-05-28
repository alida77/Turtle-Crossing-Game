from turtle import Turtle

LEVEL_FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=GAME_OVER_FONT)

    def update_scoreboard(self):
        self.goto(-240, 270)
        self.write(f"Level: {self.current_level}", align="center", font=LEVEL_FONT)

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.update_scoreboard()
