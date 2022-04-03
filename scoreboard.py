from turtle import Turtle
FONT_SIZE = 20
FONT = ("Arial", FONT_SIZE, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.update_score(self.score)

    def update_score(self, new_score):
        if new_score > 0:
            self.clear()
            self.write(f"Score: {new_score}", align="center", font=FONT, move=False)
        else:
            self.write(f"Score: {new_score}", align="center", font=FONT, move=False)


    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over.", align="center", font=FONT, move=False)