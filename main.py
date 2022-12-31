import turtle
import string
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

state_data = pandas.read_csv('50_states.csv')
#print(state_data)
states_series = state_data['state']
#print(states_series)
remaining_states = states_series.tolist()
#print(states_list)
state_count = 0
state_writer = StateWriter()
game_is_on = True
win_status = False
while game_is_on:
    answer_state = screen.textinput(title = f"{state_count}/50 States Correct", prompt = "What's another state's name?")
    cap_answer_state = string.capwords(answer_state)
    if cap_answer_state in remaining_states:
        #print("It is a U.S. state")
        state_row = state_data[state_data['state'] == cap_answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        #print(state_row)
        #print(f"x_cor = {x_cor}")
        #print(f"y_cor = {y_cor}")
        state_writer.write_state(state = cap_answer_state, x_cor = x_cor, y_cor = y_cor)

        #print(type(x_cor))
        state_count += 1
        #print(remaining_states)
        remaining_states.remove(cap_answer_state)
        #print(remaining_states)
        if state_count >= 50:
            print("You win!")
            win_status = True
            game_is_on = False
        #TODO if state_count == 50, enact win condition and game_is_on = False

    else:
        #print("It is not a U.S. state")
        pass

state_writer.end_screen(win_status)

screen.exitonclick()




#print(cap_answer_state)
#print(answer_state)

