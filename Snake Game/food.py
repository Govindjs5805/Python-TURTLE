import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5)
        self.reset()
    def reset(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
