from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


def calculate():
    distance = float(miles_input.get()) * 1.609
    km_result_label.config(text=f"{distance}")


miles_label = Label(text=" Miles", font=("Aerial", 16))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text=" is equal to ", font=("Aerial", 16))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text='0', font=("Aerial", 16))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Aerial", 16))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
