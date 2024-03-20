from tkinter import *
from tkinter import messagebox

from password_mngr import password_mngr as pwmng

FONT = ("Helvetica", 12, "normal")


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        # logo
        logo = PhotoImage(file="logo.png")

        # canvas for logo
        canvas = Canvas(width=200, height=200)
        canvas.config(highlightthickness=0)
        canvas.create_image(100, 100, image=logo)
        canvas.grid(row=0, column=1)

        # labels
        website_lbl = Label(self.window, text="Website:", font=FONT)
        username_lbl = Label(self.window, text="Email/ Username:", font=FONT)
        password_lbl = Label(self.window, text="Password:", font=FONT)

        # Entries
        self.website_entry = Entry(self.window, width=35)
        self.username_entry = Entry(self.window, width=48)
        self.password_entry = Entry(self.window, width=35)

        # Buttons
        generate_password = Button(self.window, text="Generate", font=FONT, command=self.generate_pw)
        find_password = Button(self.window, text="Search", font=FONT, command=self.find_pw, width=7, height=1)
        add_password = Button(self.window, text="Add", font=FONT, command=self.add_pw, width=20, height=1)

        # place all components in a grid
        website_lbl.grid(row=1, column=0, sticky=N)
        username_lbl.grid(row=2, column=0, sticky=N)
        password_lbl.grid(row=3, column=0, sticky=N)

        self.website_entry.grid(row=1, column=1, columnspan=1, sticky=W)
        self.username_entry.grid(row=2, column=1, columnspan=3, sticky=W)
        self.password_entry.grid(row=3, column=1, sticky=W)

        generate_password.grid(row=3, column=2, sticky=E)

        find_password.grid(row=1, column=2, sticky=E)
        add_password.grid(row=4, column=1, columnspan=3, sticky=W)
        self.window.mainloop()

    def generate_pw(self):
        new_password = pwmng.generate_password(pwmng)
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, f"{new_password}")
        self.window.clipboard_clear()
        self.window.clipboard_append(f"{new_password}")

    def add_pw(self):
        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirmation = messagebox.askokcancel(title=f"{website} ",
                                              message=f"Username: {username}"
                                                      f"\nPassword: {password}\n"
                                                      f"Is it okay to save?")
        if confirmation == 1:
            response = pwmng.add_password(website=website, username=username, password=password)
            if response == "0":
                self.username_entry.delete(0, END)
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showinfo("Success!", "Password added successfully")

            elif response == "404":
                messagebox.showerror("Error", f"Missing entry")

    def find_pw(self):
        website = self.website_entry.get().strip() + ""
        username, password = pwmng.find_password(website=website)
        if username == "not found":
            messagebox.showerror("Error", "Password not found")
        else:
            # clear the entries
            self.password_entry.delete(0, END)
            self.username_entry.delete(0, END)
            messagebox.showinfo(f"{website}", "Password found")
            self.password_entry.insert(END, f"{password}")
            self.username_entry.insert(END, f"{username}")
