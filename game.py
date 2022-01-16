import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Array for the questions, and the information about the fails
questions_information = {
    "easy": {
        "questions": [
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1"
        ],

        "max_fails": 0,

        "user_fails": 0,

        "questions_made": False
    },

    "medium": {
        "questions": [
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1"
        ],

        "max_fails": 0,

        "user_fails": 0,

        "questions_made": False
    },

    "hard": {
        "questions": [
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1",
            "1 + 1"
        ],

        "max_fails": 1,

        "user_fails": 0,

        "questions_made": False
    }
}


user_difficulty = tk.StringVar(value="easy") # WHich difficulty the user is on
highest_difficulty = tk.StringVar()

user_sum_answers = [] # All the sum answers of the user


# Clear the window
def clear_window():
    for item in window.winfo_children():
        item.destroy()


# Make the head label
def make_label(text:str):
    tk.Label(text=text, font=('arial', 14)).grid(row=0, pady=('0', '10'), columnspan=2) # Make the question and add it to the window    


# Make the submit button
def make_submit(command):  
    tk.Button(text='submit', bg='gray', font=('arial', 10), command=command).grid(sticky='EW', columnspan=2, pady=('10', '0'))


if __name__ == "__main__":
    pass