from tkinter import *
from random import choice
import pandas


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
word_dict = {}
try:
    file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = file.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    card_can.itemconfig(card_img, image=CARD_FRONT)
    card_can.itemconfig(card_title, text="French", fill="black")
    card_can.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_can.itemconfig(card_img, image=CARD_BACK)
    card_can.itemconfig(card_title, text="English", fill="white")
    card_can.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    word_dict.remove(current_card)
    pandas.DataFrame(word_dict).to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashing")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(4000, func=flip_card)

CARD_FRONT = PhotoImage(file="./images/card_front.png")
CARD_BACK = PhotoImage(file="./images/card_back.png")
card_can = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = card_can.create_image(410, 270, image=CARD_FRONT)
card_title = card_can.create_text(400, 150, text="", font=LANG_FONT, fill="black")
card_word = card_can.create_text(400, 263, text="", font=WORD_FONT, fill="black")
card_can.grid(row=0, column=0, columnspan=2, pady=50, padx=50)


correct_ans = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_ans, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=0)

wrong_ans = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_ans, highlightthickness=0, padx=50, pady=50, command=is_known)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
