COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        for i in range(10):
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1,2)
            car.goto(random.randint(-230,230), random.randint(-230,230))
            car.setheading(180)
            self.cars.append(car)
    
    
    def summon_car(self,score):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1,2)
            car.goto(280, random.randint(-230,230))
            for i in range(0, len(self.cars)):
                if car.distance(self.cars[i]) < 20:
                    car.goto(280, random.randint(-230,230))
                    i = 0
            car.setheading(180)
            self.cars.append(car)  
        
    
    def move_car(self, score):
        for i in self.cars:
            i.forward(STARTING_MOVE_DISTANCE + (score * MOVE_INCREMENT)) 
