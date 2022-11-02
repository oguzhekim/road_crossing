import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# Create Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
# Create Turtle
turtle = Player()
screen.onkeypress(turtle.move, "Up")
screen.listen()
# Create car manager
car_manager = CarManager()
# Create Scoreboard
score = Scoreboard()
# Game
game_is_on = True
while game_is_on:
    car_manager.car_count += 1
    car_manager.create_car()
    time.sleep(0.05)
    screen.update()
    car_manager.move()
    if turtle.level_up():
        car_manager.level_up()
        score.level_up()
    for car in car_manager.cars:
        if turtle.collision_with_car(car):
            screen.update()
            score.game_over()
            game_is_on = False
screen.exitonclick()
