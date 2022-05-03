
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.penup()
        self.car = []
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(0, -270)

    def move(self):
        self.if_collision()
        self.forward(10)

    def if_collision(self):
        for i in self.car:
            if i.distance(self.pos()[0], self.pos()[1]) < 25:
                self.game_is_on = False


