from turtle import Turtle

class Scoreboard(Turtle):
    score = - 1
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.add_score()
        
    def add_score(self):
        self.clear()
        Scoreboard.score += 1
        self.score = Scoreboard.score
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 20, "normal"))