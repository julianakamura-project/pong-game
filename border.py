from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.fillcolor("")
        self.pencolor("white")
        self.shapesize(stretch_wid=30, stretch_len=40)
        self.penup()

class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=-300)
        self.write(arg="|\n"
                       "|\n"
                       "|\n"
                       "|\n"
                       "|\n"
                       "|\n",
                   move=False,
                   align="center",
                   font=("courier", 50, "bold")
                   )