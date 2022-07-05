from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TIME_INCREASE = 0.5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.1
        self.start = STARTING_POSITION
        self.finish = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color("green")
       # self.current = self.ycor()

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_player_down(self):
        if self.ycor() > - 280:
            old_y = self.ycor() - MOVE_DISTANCE

            self.goto(self.xcor(), old_y)

    def start_pos(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

    def increase_speed(self):
        self.speed *= TIME_INCREASE
