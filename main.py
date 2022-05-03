import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager

# from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

count = 1

while player.game_is_on:
    if count == 5:
        new_car = CarManager()
        player.car.append(new_car)
        count = 1
    for i in player.car:
        player.if_collision()
        i.move()
        player.if_collision()

    time.sleep(0.1)
    screen.update()
    count += 1

if not player.game_is_on:
    game_over = Turtle()
    game_over.write("Game Over")

screen.exitonclick()
