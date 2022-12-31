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

    def end_screen(self, win_status):
        if win_status:
            self.goto(0,0)
            self.color('white')
            self.write("You win!🏅", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "bold"))
            self.color('black')
            self.write("You win!🏅", move = False, align = 'center', font = ("Deja Vu Sans Mono", 30, "normal"))

