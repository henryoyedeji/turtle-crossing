from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager():
    def __init__(self):
        self.allcars = []


    def draw_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            car.color(random.choice(COLORS))
            self.allcars.append(car)

    def move_car(self):
        for car in self.allcars:
            car.backward(STARTING_MOVE_DISTANCE)
            car_position = (car.xcor, car.ycor)
            # new_x = car.xcor() - STARTING_MOVE_DISTANCE
            # car.goto(new_x, car.ycor())
