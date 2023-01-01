from turtle import Turtle
FONT = ("Courier", 8, "normal")

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        
    def write_state(self, state, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(state, align = 'center', font = FONT)

    def end_screen(self, win_status, remaining_states, state_data):
        if win_status:
            self.goto(0,0)
            self.color('white')
            self.write("You win!🏅", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "bold"))
            self.color('black')
            self.write("You win!🏅", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "normal"))

        if win_status == False:
        
            correct_states = 50 - (len(remaining_states))
            for state in remaining_states:
                row = state_data[state_data.state == state]
                x_cor = int(row.x)
                y_cor = int(row.y)
                self.goto(x_cor, y_cor)
                self.color('red')
                self.write(state, align = 'center', font = FONT)

            self.goto(0,280)
            self.color('white')
            self.write(f"{correct_states} / 50 States Correct", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "bold"))
            self.color('black')
            self.write(f"{correct_states} / 50 States Correct", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "normal"))

