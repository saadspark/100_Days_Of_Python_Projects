from turtle import Turtle , Screen

new_turtle = Turtle()

for _ in range(14):
    new_turtle.forward(10)
    new_turtle.penup()
    new_turtle.forward(10)
    new_turtle.pendown()
    new_turtle.forward(10)

screen = Screen()
screen.exitonclick()