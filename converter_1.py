from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"            #Just added background colort to the GUI
YELLOW = "#f7f5dd"

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)
window.config(bg=GREEN)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


def calculate():
    distance = float(miles_input.get()) * 1.609
    km_result_label.config(text=f"{round(distance, 2)}")


miles_label = Label(text=" Miles", font=("Aerial", 16), highlightthickness=0, bg=GREEN)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text=" is equal to ", font=("Aerial", 16), highlightthickness=0, bg=GREEN)
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text='0', font=("Aerial", 16), highlightthickness=0, bg=PINK)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Aerial", 16), highlightthickness=0, bg=GREEN)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate, highlightthickness=0, bg=YELLOW)
calculate_button.grid(column=1, row=2)

window.mainloop()
