# importing modules
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=400, height=400)
color = ["red", "green", "yellow", "blue", "orange", "purple"]

# ask user to choose which color will win the race
user_bet = screen.textinput(title="make your bet", prompt="which color turtle will win options are red blue green "
                                                          "yellow blue orange or purple ")
is_race_on = False

# make turtle line up in the start line
start_point_x = - 170
start_point_y = - 100
turtles = []

# create a list of turtle for the race
for turtle_num in range(0, 6):
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(color[turtle_num])
    turtle_name.goto(x=start_point_x, y=start_point_y)
    start_point_y += 40
    turtles.append(turtle_name)

# starting the race and printing the winner
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 160:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
