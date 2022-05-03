from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.goto(300, random.randrange(-250, 250, 20))
        self.color(random.choice(COLORS))

    def move(self):
        self.back(STARTING_MOVE_DISTANCE)




