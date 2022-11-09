from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/spanish_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Spanish", fill="black")
    canvas.itemconfig(word_text, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(spanish_word_card, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(spanish_word_card, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"],fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/spanish_words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
spanish_word_card = canvas.create_image(400, 253, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_back_image = PhotoImage(file="images/card_back.png")
title_text = canvas.create_text(400, 150, text="Title", font=("Aerial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Aerial", 60, "bold"))

known_button_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
