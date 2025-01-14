import turtle
import pandas
from turtle import Screen, Turtle
screen = Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="what other state name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = data[data.state == answer_state]
        state_name.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        state_name.write(answer_state)

screen.exitonclick()
