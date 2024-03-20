import pandas as pd
import turtle as tt

# setup screen
screen = tt.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
tt.shape(image)
tt.up()
tt.tracer(0)

# get state names and coordinates
states_temp = pd.read_csv("50_states.csv").to_dict()

# change format
states = {}
for i in range(50):
    states[f"{states_temp['state'][i].lower()}"] = (states_temp["x"][i], states_temp["y"][i])


# gameplay

def write_text(cors=(0, 0), text="", font_size=7):
    tt.goto(cors)
    tt.write(text, align="center", font=("Ariel", font_size, "normal"))
    tt.goto(0, 0)
    tt.update()

def write_all_states():
    tt.color("red")
    for state in states:
        tt.goto(states[state])
        tt.write(f"{state.capitalize()}", align="center", font=("Ariel", 7, "normal"))
    tt.goto(0,0)
    tt.update()

correct_answers = 0
NUMBER_OF_STATES = 50
game_is_on = True

while game_is_on:
    try:
        guess = tt.textinput(f"{correct_answers}/{NUMBER_OF_STATES} states correct",
                             "Enter a state name:\n(enter 'quit' to end the game)").lower()
    except:
        continue

    if guess == "quit":
        game_is_on = False

        write_text((-20,250), f"You found {correct_answers} out of 50 states names", font_size=20)
        write_all_states()
    elif guess in states:
        correct_answers += 1
        write_text(states[guess], f"{guess.capitalize()}")
        states.pop(guess)
    else:
        continue

    if correct_answers == 50:
        game_is_on = False
        tt.goto(-20, 0)
        tt.write("Congratulations, you found all of states names!", align="center", font=("Ariel", 20, "normal"))
screen.exitonclick()
