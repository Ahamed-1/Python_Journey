import pandas
import turtle

image = './day_25/blank_states_img.gif'
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
# Turtle will only support gif images 
# The above five lines of code will create a screen with the U.S. map as the background image.

map_turtle = turtle.Turtle()
map_turtle.penup()
map_turtle.hideturtle()

data = pandas.read_csv('./day_25/50_states.csv')
all_states = data['state'].to_list()
score = 0
found_states = []

while len(found_states) < 50:
        
    answer_state = screen.textinput(title=f"{score}/50 found", prompt="Guess the States.").title()
    if answer_state == 'Exit':
        missed_states = [state for state in all_states if state not in found_states]
        dataframe = pandas.DataFrame({'Missed' : missed_states})
        dataframe.to_csv('./day_25/new_data.csv')
        break
    if answer_state in all_states:
        if answer_state not in found_states:
            found_states.append(answer_state)

            guess_state = data[data.state == answer_state]
            new_x = guess_state.x.item() # This will give the value of the x column
            new_y = guess_state.y.item()

            map_turtle.goto(new_x,new_y)
            map_turtle.write(answer_state, align='center', font=('Arial', 10, 'normal'))
            score += 1
