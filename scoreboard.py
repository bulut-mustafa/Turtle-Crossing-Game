from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-230,260)
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align= 'center', font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align= 'center', font=FONT)