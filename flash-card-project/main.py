from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


def new_word():
    global another_word, timer
    window.after_cancel(timer)
    another_word = random.choice(data_dict)
    canvas.itemconfig(word_text, text=another_word['French'], fill="black")
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(card_image, image=card_front)
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=another_word['English'], fill="white")


def right_click():
    global another_word
    new_word()
    data_dict.remove(another_word)
    df = pd.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)


def left_click():
    new_word()


data = pd.read_csv("data/french_words.csv")
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    pass
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
finally:
    data_dict = data.to_dict(orient="records")
    another_word = random.choice(data_dict)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
left_image = PhotoImage(file="images/wrong.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=another_word["French"], font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_image, highlightthickness=0, command=right_click)
left_button = Button(image=left_image, highlightthickness=0, command=left_click)
right_button.grid(column=1, row=1)
left_button.grid(column=0, row=1)

timer = window.after(3000, flip_card)

window.mainloop()
