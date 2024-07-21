from turtle import Turtle,Screen
import random



screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','blue','yellow','pink','silver','green']
y = [-70,-40,-10,20,50,80]
is_race_on = False

turtle_list = []
for i in  range(0,6):
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=y[i])
    turtle_list.append(new_turtle)

if user_bet :
    is_race_on = True

while  is_race_on:
    random_distance = random.randint(0, 20)
    for turtle in turtle_list :
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've won! The {winning_color} turtle is the winner!")
            else :
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random_distance)


screen.exitonclick()