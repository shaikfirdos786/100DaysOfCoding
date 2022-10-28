import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(play.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if play.distance(car) < 20:
            score.if_game_over()
            game_is_on = False

    # Detect collision with finish line
    if play.is_at_finish_line():
        play.restart_turtle()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
