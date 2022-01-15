import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Array for the questions, and the information about the fails
questions_information = {
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
question_answers = []


# Clear the window
def clear_window():
    for item in window.winfo_children():
        item.destroy()


# Make the head label
def make_label(text):
    tk.Label(text=text, font=('arial', 14)).grid(row=0, pady=('0', '10'), columnspan=2) # Make the question and add it to the window    


# Make the submit button
def make_submit(command):  
    tk.Button(text='submit', bg='gray', font=('arial', 10), command=command).grid(sticky='EW', columnspan=2, pady=('10', '0'))


# Make the input(s)
def make_input(input_type:str, array):
    # Check if the given array is a function that must be called
    try:
        array = array()
    
    # If it is not a function that must be called
    except TypeError:
        pass


    if input_type == "spinbox":
        for row, question in enumerate(array):
            question_row = row + 1 # Row of the question label + input

            # Add all the answers to a list
            answer = tk.StringVar()
            question_answers.append(answer)


            tk.Label(text=question, font=('arial', 14)).grid(row=question_row, column=0, pady=('0', '10')) # Input label
            tk.Spinbox(window, textvariable=answer, from_=0, to=float('inf')).grid(row=question_row, column=1) # Input

    elif input_type == "radiobutton":
        for row, difficulty_option in enumerate(array):
            ttk.Radiobutton(window, text=difficulty_option, value=difficulty_option, variable=chosen_difficulty).grid(sticky='e') # Input


# Return the questions of the difficulty the user is in
def make_difficulty_questions():
    questions = questions_information[chosen_difficulty.get()]['questions'] # ALl the questions for the difficulty the user is in

    return questions # Return the questions


def show_questions():   
    clear_window()
    make_label(f"Calculate the questions on the screen")
    make_input("spinbox", make_difficulty_questions)
    make_submit("")



def choose_gamemode():
    make_label("Choose the starting difficulty")
    make_input("radiobutton", questions_information)
    make_submit(show_questions)




# When the program starts
if __name__ == "__main__":
    choose_gamemode()
    window.mainloop()