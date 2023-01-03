from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-120, -80, -40, 0, 40, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-210, y=y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print("Your bet is correct!")
            else:
                print(f"Wrong! {winning_color} won this time.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)










screen.exitonclick()
