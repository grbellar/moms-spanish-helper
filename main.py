import pandas
import tkinter as tk
from tkinter import messagebox
import os

# TODO: validation

image_path = os.path.abspath("./images/card_front.png")
csv_data_path = os.path.abspath("./spanish-data.csv")

BACKGROUND_COLOR = "#B1DDC6"
HEADING_LABEL = ("Verdana", 14, "italic")
WORD_LABEL = ("Verdana", 18, "normal")
BUTTON_LABEL = ("Verdana", 12, "normal")
# only parse required columns to save memory
REQ_COLS = ["word_spanish", "word_english", "mood_english", "tense_english", "yo", "tu", "el/ella", "ellos"]


def read_data(word: str, tense: str):
    data_df = pandas.read_csv(csv_data_path, usecols=REQ_COLS)
    # word_df = data_df[data_df["word_spanish"] == word]
    # allows for spanish or english word entry
    for (index, series) in data_df.iterrows():
        if word in series["word_english"] and series["mood_english"] == "Indicative" and series["tense_english"] == tense:
            print(type(series))
            print(series)
            return series
        # problem with this is i need it to search for the exact match in the mood_spanish column and not a just a substring
        elif series["mood_english"] == "Indicative" and series["tense_english"] == tense:
            print(type(series))
            print(series)
            return series
        # # use mood to ensure there is only one result for each tense
        # mood_df = word_df[word_df["mood_english"] == "Indicative"]
        # # pull the user chosen tense of the word
        # word_series = mood_df[mood_df["tense_english"] == tense]
        # print(type(word_series))
        # print(word_series)
        # return word_series


def update_display(word: str, tense: str):
    word_series = read_data(word, tense)
    if len(word_series) == 0:
        messagebox.showinfo(title=None,
                            message="Word not found. Please check the spelling and try again. Or perhaps the word is "
                                    "not in the database.")
    else:
        yo = word_series["yo"].item()
        canvas.itemconfig(yo_word, text=yo)
        tu = word_series["tu"].item()
        canvas.itemconfig(tu_word, text=tu)
        el_ella = word_series["el/ella"].item()
        canvas.itemconfig(el_ella_word, text=el_ella)
        ellos_ellas = word_series["ellos"].item()
        canvas.itemconfig(ellos_ellas_word, text=ellos_ellas)
        definition.config(text=word_series["word_english"].item())


root = tk.Tk()
root.config(padx=50, pady=25, bg=BACKGROUND_COLOR)
root.title("MCH")

# ui
# -------------------------------------------------------------------------------------#
canvas = tk.Canvas(width=1000, height=551, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = tk.PhotoImage(file=image_path)
background = canvas.create_image(400, 268, image=card_image)
canvas.grid(column=0, row=0, columnspan=5)

yo_label = canvas.create_text(100, 150, text="yo", font=HEADING_LABEL)
tu_label = canvas.create_text(100, 250, text="tu", font=HEADING_LABEL)
el_ella_label = canvas.create_text(100, 350, text="el/ella", font=HEADING_LABEL)
ellos_label = canvas.create_text(100, 450, text="ellos/ellas", font=HEADING_LABEL)
word_label = canvas.create_text(300, 50, text="Mom's Conjugation Helper", font=("Impact", 36, "normal"))

yo_word = canvas.create_text(300, 150, text="", font=WORD_LABEL)
tu_word = canvas.create_text(300, 250, text="", font=WORD_LABEL)
el_ella_word = canvas.create_text(300, 350, text="", font=WORD_LABEL)
ellos_ellas_word = canvas.create_text(300, 450, text="", font=WORD_LABEL)

# buttons
present = tk.Button(text="present", font=BUTTON_LABEL, command=lambda: update_display(usr_input.get(), "Present"))
future = tk.Button(text="future", font=BUTTON_LABEL, command=lambda: update_display(usr_input.get(), "Future"))
imperfect = tk.Button(text="imperfect", font=BUTTON_LABEL, command=lambda: update_display(usr_input.get(), "Imperfect"))
conjugate = tk.Button(text="conjugate!", font=BUTTON_LABEL, command=lambda: update_display(usr_input.get(), "Present"))
present.grid(column=0, row=1, sticky="EW")
future.grid(column=1, row=1, sticky="EW")
imperfect.grid(column=2, row=1, sticky="EW")
conjugate.grid(column=4, row=1, sticky="EW")

# definition display
definition = tk.Label(text="", font=("Verdana", 16, "normal"), bg=BACKGROUND_COLOR, padx=25, pady=25)
definition.grid(column=0, row=2, columnspan=3)

# user entry
usr_input = tk.Entry(width=14, font=("Verdana", 16, "normal"))
usr_input.grid(column=3, row=1)

root.mainloop()
