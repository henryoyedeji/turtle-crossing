import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race")
screen.tracer(0)

# for i in range(4):
#     timi = Turtle()


cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")
screen.onkey(player.move_player_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(player.speed)
    screen.update()
    cars.draw_car()
    cars.move_car()

    for car in cars.allcars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # player.start_pos()

    # Check if player has crossed finish line and increase level
    if player.ycor() > player.finish:
        score.add_score()
        player.goto(player.start)
        player.speed *= 0.5

# game_is_on = True
# while game_is_on:
#     time.sleep(player.speed)
#     screen.update()
#     play_game()
#     for car in cars.allcars:
#         if car.distance(player) < 20:
#             score.game_over()
#             game_is_on = False
#             user_input = screen.textinput(title="Play again",
#                                         prompt="Would you like to play again? Y/N ").lower()
#             if user_input == "y":
#                 screen.clear()
#                 game_is_on=True
#                 # player.goto(player.start)
#                 # screen.clear()
#                 # score.score = 1
#
#                 play_game()


screen.exitonclick()
