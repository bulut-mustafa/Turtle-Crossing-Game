import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.summon_car(scoreboard.score)
    car_manager.move_car(scoreboard.score)
    
    for car in car_manager.cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 290:
        player.starting_position()
        scoreboard.score +=1
        scoreboard.update_score()
    

screen.exitonclick()