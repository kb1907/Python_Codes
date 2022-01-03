from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------- NEW WORD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(lang_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=background_image)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(lang_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=flip_card_image)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_image = PhotoImage(file="images/card_front.png")
flip_card_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(450, 263,
                                   image=background_image)  # We put x and y coordinates as almost half of the canvas
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
lang_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
dont_know_image = PhotoImage(file="images/wrong.png")
button_dont_know = Button(image=dont_know_image, highlightthickness=0, command=next_card)
button_dont_know.grid(column=0, row=1)
button_right_image = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

next_card()
window.mainloop()
