from turtle import Turtle, Screen
import pandas as pd 

screen = Screen()
image = "Day-25-us-states-game-panadas/blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

states = pd.read_csv("Day-25-us-states-game-panadas/50_states.csv")


game_is_on = True
count = len(states)

while game_is_on:
    entered_state = screen.textinput(title=f" {count}/50 Guess the State", prompt="What's another state's name?").title()
    count -= 1
    if count == 0 or entered_state == 'Exit':
        game_is_on = False

    val =  states[states.state == entered_state]
    if len(val) > 0 :

        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(val.x), int(val.y))
        turtle.write(entered_state)



screen.title("U.S. States Game")

screen.exitonclick()