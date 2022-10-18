import turtle
import pandas
# import turtle as t

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
# # screen.exitonclick()

guessed_state = []

count = 1
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="Whats another states name").title()
    print(answer_state)

    if answer_state == "Exit":

        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        # OR
        missing_states = [state for state in all_states if state not in guessed_state]

        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]       # Extracting row of the answer
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # print(int(state_data.x))
        # print(int(state_data.y))
        #Create a turtle to write the name of the state at the states x and y coordinate.


# States to learn.csv
# while answer_state