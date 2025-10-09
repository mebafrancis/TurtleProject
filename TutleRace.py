from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on= False
screen.setup(500, 400)
user_bet= screen.textinput(title="Make your bet", prompt="Which turtle will win")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
print(user_bet)
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=Y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()