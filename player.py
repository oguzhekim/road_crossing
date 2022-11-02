from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_location()
        self.setheading(90)
        self.level = 1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def collision_with_car(self, car):
        if car.ycor() <= self.ycor() + 10 and self.distance(car) < 30:
            return True
        elif car.xcor() < 30 and self.distance(car) < 30:
            return True

    def level_up(self):
        if self.ycor() > 280:
            self.level += 1
            self.reset_location()
            return True

    def reset_location(self):
        self.goto(STARTING_POSITION)