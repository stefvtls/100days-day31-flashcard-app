import tkinter
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TO_LEARN = "Dutch"
LANGUAGE_NATIVE = "English"
FONT_TOP = ("Ariel", 40, "italic")
FONT_BOTTOM = ("Ariel", 60, "bold")
Y_TXT_COORDINATES_TOP = 150
Y_TXT_COORDINATES_BOTTOM = 263
X_TXT_COORDINATES = 400

# APP LAYOUT
window = tkinter.Tk()
window.minsize(width=900, height=626)
window.title("Learn Dutch fast - 5000 most common used words in movie subtitles")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_card = tkinter.PhotoImage(file="images/card_front.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_image = tkinter.PhotoImage(file="images/right.png")
card = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card.create_image(0, 0, anchor="nw", image=front_card)
language_front = card.create_text(X_TXT_COORDINATES,Y_TXT_COORDINATES_TOP, text=LANGUAGE_TO_LEARN, font=FONT_TOP)
word_front = card.create_text(X_TXT_COORDINATES,Y_TXT_COORDINATES_BOTTOM, text="test word", font=FONT_BOTTOM)
card.grid(row=0, column=0, columnspan=2)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0)
right_button = tkinter.Button(image=right_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()
