import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Array for the questions, and the information about the fails
question_information = {
    "easy": {
        "questions": [
            "1 + 1",
            "3 - 5",
            "52 + 9",
            "-7 + 32",
            "65 - 96"
        ],

        "max_fails": 0,

        "user_fails": 0
    },

    "medium": {
        "questions": [
            "154 / 2",
            "327 + 637",
            "-643 + 960",
            "404 + 329",
            "330 * 3"
        ],

        "max_fails": 0,

        "user_fails": 0
    },

    "hard": {
        "questions": [
            "503 + 3965",
            "-5964 + 9773",
            "32 * 135",
            "1740 / 6",
            "596 * 9"
        ],

        "max_fails": 1,

        "user_fails": 0
    }
}


chosen_difficulty = tk.StringVar(value="easy")


# Make the question
def make_label(text):
    tk.Label(text=text, font=('arial', 14)).grid(row=0, pady=('0', '10')) # Make the question and add it to the window    


# Make the submit button
def make_submit():  
    tk.Button(text='submit', bg='gray', font=('arial', 10), command=show_questions).grid(sticky='EW', pady=('10', '0'))


def show_questions():   
    questions = question_information[chosen_difficulty.get()]['questions']

    print(questions)





def gamemode_options():
    for row, difficulty_option in enumerate(question_information):
        question_row = row + 1

        ttk.Radiobutton(window, text=difficulty_option, value=difficulty_option, variable=chosen_difficulty).grid(row=question_row) # Input



def choose_gamemode():
    make_label("Choose the starting difficulty")
    gamemode_options()
    make_submit()




# When the program starts
if __name__ == "__main__":
    choose_gamemode()
    window.mainloop()