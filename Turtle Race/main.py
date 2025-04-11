from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
x = - 230
y = - 100
for index, color in enumerate(colors):
    muqi = Turtle("turtle")
    muqi.penup()
    muqi.goto(x=x,y=y)
    y += 35
    muqi.color(colors[index])
    turtles.append(muqi)
is_raceon = True

while is_raceon:
    for turt in turtles:
        if turt.xcor() > 230:
            is_raceon = False
            winning_colour = turt.pencolor()
            if user_bet == winning_colour:
                print(f"You Win. The {winning_colour} is the winner")
                break
            else:
                print(f"You've lost the match. The {winning_colour} is the winner")
                break

        turt.forward(randint(10, 25))
        
screen.exitonclick()