from tkinter import *
import re

FONT = ("Calibri", 12, "normal")
# root window
window = Tk()
window.title("Miles to kilometers")
window.minsize(width=300, height=140)
window.config(padx=30, pady=30)


def convert():
    miles = miles_entry.get().strip()
    # check if it is float or numeric
    if re.match("\d+[.]\d+", miles) or miles.isnumeric():
        km_result.config(text=eval(miles) * 1.6)
    else:
        km_result.config(text="wrong input")


# entry
miles_entry = Entry()
miles_entry.grid(row=0, column=1)

# entry label
entry_label = Label(text="miles", font=FONT)
entry_label.grid(row=0, column=2)

# equal label
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

# kilometers label
km_result = Label(text="0", font=FONT)
km_result.grid(row=1, column=1)

# km label
km_label = Label(text="kilometers", font=FONT)
km_label.grid(row=1, column=2)

# conversion button
convert_button = Button(text="Calculate", font=FONT, command=convert)
convert_button.grid(row=2, column=1)

window.mainloop()
