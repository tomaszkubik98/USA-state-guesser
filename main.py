import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)



data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = 0

game_on = True
while game_on:
    answer = screen.textinput(f"Guessed states {guessed_states}/50", "Type missing state:").title()
    if answer == "Exit":
        missed_states = pandas.DataFrame(states_list)
        missed_states.to_csv("states_to_learn.csv")
        break
    if answer in states_list:
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        new_x = (data[data.state == answer]).x
        new_y = (data[data.state == answer]).y
        timmy.goto(int(new_x)-10,int(new_y))
        timmy.write(answer)
        states_list.remove(answer)
        guessed_states += 1

    if states_list == []:
        game_on = False

turtle.mainloop()






