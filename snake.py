from turtle import Turtle
from time import sleep
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake():
    new_x = 0

    def __init__(self):
        self.segments = []
        Snake.new_x -= 20
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for i in range(5):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(self.new_x, 0)
            self.segments.append(new_snake)
        
    def move(self):
        
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        
        self.head.forward(20)
    
    def detect_collision_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        
    
    def add_tail(self):
        tail = Turtle(shape="square")
        tail.color("white")
        tail.penup()
        self.segments.append(tail)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

        