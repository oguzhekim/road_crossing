from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 1
        self.car_count = 0

    def move(self):
        for car in self.cars:
            car.forward((STARTING_MOVE_DISTANCE + (self.level-1) * MOVE_INCREMENT))

    def create_car(self):
        if self.car_count % 6 == 0:
            new_car = Turtle()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(310, randint(-245, 280))
            self.cars.append(new_car)

    def level_up(self):
        self.level += 1
