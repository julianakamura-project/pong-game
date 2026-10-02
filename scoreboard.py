from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
SIZE = 50
STYLE = "bold"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=230)
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.left_score} : {self.right_score}",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, SIZE, STYLE)
                   )

    def increase_l_score(self):
        self.left_score +=1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.right_score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, SIZE, STYLE))