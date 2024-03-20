import pandas as pd
from tkinter import *
import random
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Helvetica", 35, "bold")
NUMBER_OF_WORDS = 5
learned_words = 0
countdown = None
# # --------------------FILE HANDLING -------------------# #
def get_flashcards():
    """
    returns french and english words,\n
    index corresponding to translation
     """
    data = pd.read_csv("data/french_words.csv")
    french = random.choices(data.French.values, k=NUMBER_OF_WORDS)
    english = random.choices(data.English.values, k=NUMBER_OF_WORDS)
    return list(french), list(english)


french, english = get_flashcards()

# # --------------------END FILE HANDLING -------------------# #


# # -------------------- FUNCTIONS -------------------# #
def right_answer():
    global french, english, learned_words
    if canvas.itemcget(lang_text, "text")=="english":
        learned_words += 1
        current_word = canvas.itemcget(word_text, "text")
        current_index = english.index(current_word)
        show_fr(current_index+1)


def wrong_answer():
    global french, english
    if canvas.itemcget(lang_text, "text") == "english":
        current_word = canvas.itemcget(word_text, "text")
        current_index = english.index(current_word)
        french.insert(len(french)-1,french[current_index])
        english.insert(len(french)-1,english[current_index])
        show_fr(current_index + 1)


def flip_card(lang, current_word):
    if lang=="english":
        canvas.itemconfigure(word_text, text=f"{current_word}", fill="white", font=FONT)
        canvas.itemconfigure(lang_text, text="english", fill="white")
        canvas.itemconfigure(canvas_img, image=card_back)
    elif lang=="french":
        canvas.itemconfigure(word_text, text=f"{current_word}", fill="black", font=FONT)
        canvas.itemconfigure(lang_text, text="french", fill="black")
        canvas.itemconfigure(canvas_img, image=card_front)


def show_fr(indx=0):
    global countdown
    if indx > len(french)-1:
        end_session()
    current_word = french[indx]
    flip_card("french", current_word)
    countdown = window.after(5000, show_en, indx)


def show_en(indx):
    start_button.grid_forget()
    current_word = english[indx]
    flip_card("english", current_word)


def start_session():
    start_button.grid_remove()
    end_button.grid(row=2, column=1, columnspan=2)
    show_fr(0)


def end_session():
    warning = messagebox.askyesno("End session", "Are you sure you want to end session?\n"
                                                 "The deck will be shuffled in the new session")
    if not warning:
        return None
    global learned_words
    if countdown is not None:
        window.after_cancel(countdown)
    canvas.itemconfigure(lang_text, text=f"You learned\n          {learned_words} \nwords today")
    canvas.itemconfigure(word_text, text="")
    end_button.grid_remove()
    start_button.grid(row=2, column=1, columnspan=2)
    learned_words = 0
# # -------------------- END FUNCTIONS -------------------# #


# # -------------------- GUI -------------------# #
window = Tk()
window.title("Flashy")
window.config(padx=35, pady=35, bg=BACKGROUND_COLOR)
window.minsize(width=450, height=350)

# images
right_img = PhotoImage(file="images/right.png")
right_img = right_img.subsample(2, 2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_img = wrong_img.subsample(2, 2)

card_front = PhotoImage(file="images/card_front.png")
card_front = card_front.subsample(2)

card_back = PhotoImage(file="images/card_back.png")
card_back = card_back.subsample(2)


canvas = Canvas(width=400, height=270)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(200, 135, image=card_back)
lang_text = canvas.create_text(200, 70, font=("Helvetica", 12, "italic"), text="", fill="white")
word_text = canvas.create_text(200, 135, font=FONT, text=f"", fill="white")
canvas.grid(row=0, column=0, rowspan=1, columnspan=4)


wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=wrong_answer)
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=right_answer)
start_button = Button(text="Start", borderwidth=0, highlightthickness=0, command=start_session, width=35,
                      bg="#FCF8E8", fg="black")
end_button = Button(text="End", borderwidth=0, highlightthickness=0, command=end_session, width=35,
                      bg="#FCF8E8", fg="black")

wrong_button.grid(row=1, column=1, sticky=W)
right_button.grid(row=1, column=2, sticky=E)
start_button.grid(row=2, column=1, columnspan=3,sticky=W)

window.mainloop()
# # -------------------- END GUI -------------------# #