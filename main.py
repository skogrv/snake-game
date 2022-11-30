from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()

food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    snake.move()
    screen.update()
    
    if snake.head.distance(food) < 15:
        snake.add_tail()
        food.refresh()
        scoreboard.add_score()
        
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.detect_collision_tail():
        game_is_on = False
        scoreboard.game_over()
        
        

screen.exitonclick()

