import turtle
import time
from score import Score
from food import Food
from snake import Snake
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("SNAKE GAME")
screen.tracer(0)
score=Score()

s=Snake()
food = Food()
screen.listen()
screen.onkey(key="w", fun=s.up)
screen.onkey(key="s", fun=s.down)
screen.onkey(key="a", fun=s.left)
screen.onkey(key="d", fun=s.right)

screen.update()
over = False
while over==False:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(food) < 15:
        score.reset()
        food.reset()
        s.extend()
    if s.head.xcor()>300 or s.head.xcor()< -300 or s.head.ycor()>300 or s.head.ycor()<-300:
        score.gameover()
        score.win()
        over =True
    for i in s.snakes:
        if i==s.head:
            pass
        elif s.head.distance(i) < 10:
            over = True
            score.gameover()
            score.win()

screen.exitonclick()
