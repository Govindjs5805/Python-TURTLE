from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head=self.snakes[0]
        self.tail=self.snakes[len(self.snakes)-1]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add(position)

    def add(self,position):
        ammalu = Turtle()
        ammalu.penup()
        ammalu.shape("square")
        ammalu.color("white")
        ammalu.goto(position)
        self.snakes.append(ammalu)
    def extend(self):
        self.add(self.snakes[-1].position())



    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def right(self):
        if self.snakes[0].heading() == 270:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 90:
            self.snakes[0].right(90)

    def left(self):
        if self.snakes[0].heading() == 270:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 90:
            self.snakes[0].left(90)

    def up(self):
        if self.snakes[0].heading() == 0:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 180:
            self.snakes[0].right(90)

    def down(self):
        if self.snakes[0].heading() == 0:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 180:
            self.snakes[0].left(90)
