import turtle
from data import data, all_states
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
need_to_learn = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title= f"{len(guessed_states)} / 50 States Correct", prompt= "What's the name of a state?").title()
    
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(int(state_data.x), int(state_data.y))
        s.write(answer_state)

if len(guessed_states) < 50:
    for state in all_states:
        if state not in guessed_states:
            need_to_learn.append(state)

    states_to_learn = pandas.DataFrame(data= need_to_learn, columns=["States to Learn"])

    states_to_learn.to_csv("states_to_learn.csv")



#states_to_learn.csv