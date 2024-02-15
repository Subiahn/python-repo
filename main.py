from turtle import Turtle, Screen
import random


is_race_on = False
screen =Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Ecter a color: ")

color = ["red", "orange", "yellow","green", "blue", "purple"]
y_point = [100 , 60, 20, -20, -60, -100 ]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_point[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print(f"You've won! The {winnig_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winnig_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()




# for i, j in zip(color, y_point):
#     tim = Turtle(shape="turtle")
#     tim.color(i)
#     tim.penup()
#     tim.goto(x=-230, y=j)
#
# screen.exitonclick()
