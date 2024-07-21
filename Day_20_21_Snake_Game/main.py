from turtle import Turtle,Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Score


is_game_on = True
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while is_game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.update_core()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segment_list:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10 :
            is_game_on = False
            score.game_over()
    



screen.exitonclick()