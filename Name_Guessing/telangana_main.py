import turtle
import pandas

screen = turtle.Screen()
screen.title("Telangana state Game")
image = "telangana.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("34_districts.csv")
all_districts = data.district.to_list()
guessed_districts = []

while len(guessed_districts) < 50:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/34 Districts Correct",
                                       prompt="What's another district's name?").title()
    if answer_district == "Exit":
        missing_districts = []
        for district in all_districts:
            if district not in guessed_districts:
                missing_districts.append(district)
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break
    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer_district)
