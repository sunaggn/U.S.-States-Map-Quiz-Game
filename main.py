import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title= "Guess the State", prompt="Name another")
print(answer_state)

guess = input("What's another state name?")

states = pandas.read_csv("50_states.csv")





screen.exitonclick()