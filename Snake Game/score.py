from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.goto(-80,270)
        self.hideturtle()
        self.pencolor("white")
        self.write(f"CURRENT SCORE : {self.point}", font=FONT)

    def reset(self):
        self.clear()
        self.point+=1
        self.write(f"CURRENT SCORE : {self.point}", font=FONT)
    def gameover(self):
        self.goto(-220,0)
        self.clear()
        self.pencolor("green")
        self.write("GAME OVER !",font=("Arial", 50, "bold"))
        self.penup()
        self.goto(-220,-8)
        self.write("__________________________________________________",font=FONT)
        self.penup()
    def win(self):
        self.goto(-90,-40)
        self.pendown()
        self.pencolor("red")
        self.write(f"TOTAL SCORE : {self.point}", font=("Arial", 16, "bold"))
