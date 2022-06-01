import tkinter
import pandas
import random

# const variables
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TO_LEARN = "DUTCH"
LANGUAGE_NATIVE = "ENGLISH"
FONT_TOP = ("Ariel", 40, "italic")
FONT_BOTTOM = ("Ariel", 60, "bold")
Y_TXT_COORDINATES_TOP = 150
Y_TXT_COORDINATES_BOTTOM = 263
X_TXT_COORDINATES = 400
TIMER = 3000
ind = 0


# reading data
data = pandas.read_csv("words/NL-ENG.csv")
frequency_dictionary = data.to_dict(orient="records")
LENGTH = len(frequency_dictionary)




# button mechanism
def choose_random_word():
    global ind
    index = random.randint(0, LENGTH)
    card.itemconfig(card_background, image=front_card)
    card.itemconfig(text_top, fill="black", text=LANGUAGE_TO_LEARN)
    card.itemconfig(text_bottom, fill="black", text=frequency_dictionary[index][LANGUAGE_TO_LEARN])
    ind = index
    window.after(ms=TIMER, func=flip)


# generating translation card. stopping the timer after the flip
def flip():
    card.itemconfig(card_background, image=back_card)
    card.itemconfig(text_top, fill="white", text=LANGUAGE_NATIVE)
    card.itemconfig(text_bottom, fill="white", text=frequency_dictionary[ind][LANGUAGE_NATIVE])
    window.after_cancel()


# APP LAYOUT - creating visual user interface
# main window
window = tkinter.Tk()
window.minsize(width=900, height=626)
window.title("Learn Dutch fast - 5000 most common used words in movie subtitles")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# photo images
front_card = tkinter.PhotoImage(file="images/card_front.png")
back_card = tkinter.PhotoImage(file="images/card_back.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_image = tkinter.PhotoImage(file="images/right.png")
# canvas
card = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = card.create_image(0, 0, anchor="nw", image=front_card)
text_top = card.create_text(X_TXT_COORDINATES, Y_TXT_COORDINATES_TOP, text=LANGUAGE_TO_LEARN, font=FONT_TOP)
text_bottom = card.create_text(X_TXT_COORDINATES, Y_TXT_COORDINATES_BOTTOM, text="are you ready?", font=FONT_BOTTOM)
card.grid(row=0, column=0, columnspan=2)
# buttons
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=choose_random_word)
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=choose_random_word)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)


# loading first flash card at the beginning of the program
choose_random_word()

# timer
window.after(ms=TIMER, func=flip)

# END
window.mainloop()
