import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Array for the questions, and the information about the fails
sum_information = {
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


user_difficulty = tk.StringVar(value="easy") # Which difficulty the user is on


user_sum_answers = [] # All the sum answers of the user


# Clear everythign on the window
def clear_window():
    for item in window.winfo_children():
        item.destroy()


# Make the head label
def make_label(text:str):
    tk.Label(window, text=text, font=('arial', 14)).grid(row=0, pady=('0', '10')) # Label at the top


# Make the submit button
def make_submit(command):  
    tk.Button(window, text='submit', bg='gray', font=('arial', 10), command=command).grid(sticky='EW', columnspan=2, pady=('10', '0')) # Submit button


# Validate the answers the user gave on the questions
def validate_user_answers():
    error_made = False # If the user made an error
    user_answers = [user_answer.get() for user_answer in user_sum_answers] # Every answer of the user

    # For every question
    for user_answer in user_answers:
        # Check if it is a number
        try:
            int(user_answer) 

        # If it is not a number
        except ValueError:
            user_answer.set(0) # Reset the value of the input
            error_made = True 
    
    # If every answer is validated
    else:
        # If all the answers of the user were numbers
        if not error_made:
            error_made = False
            calculate_user_answer(user_answers) # Calculate the mistakes of the user


# Check if the user gave the good answers on the questions
def calculate_user_answer(user_answers:list):
    # Get all the answers
    difficulty = user_difficulty.get() # Difficulty the user is on
    questions = sum_information[difficulty]['questions'] # All the questions
    answers = [eval(question) for question in questions] # All the answers on the questions

    user_answers = [int(user_answer) for user_answer in user_answers] # All the answers of the user

    # For every question
    for user_answer, answer in zip(user_sum_answers, answers):
        pass



# Make the questions / show the questions on screen
def make_questions():
    difficulty = user_difficulty.get() # Difficulty the user is on
    questions = sum_information[difficulty]['questions'] # All the questions


    # Loop through every question
    for num, question in enumerate(questions):
        row = num + 1

        # Remember the answer of the user
        answer = tk.StringVar()
        user_sum_answers.append(answer)

        tk.Label(window, text=f"{question} =", font=('arial', 14)).grid(row=row, column=0, pady=('0', '10')) # Show the question before the input
        tk.Spinbox(window, textvariable=answer, from_=0, to=float('inf')).grid(row=row, column=1) # Input


# Show all the difficulties the user can choose from
def make_difficulty_options():
    difficulties = list( sum_information.keys() ) # ALl the difficulties

    # Let the user choose between all the difficulties
    for num, difficulty in enumerate(difficulties):
        row = num + 1

        ttk.Radiobutton(window, text=f"{difficulty.capitalize()}", value=difficulty, variable=user_difficulty).grid(row=row)


# Call the functions for the question screen
def question_screen():  
    clear_window() # Clear everything on the window

    make_label(f"Questions for the difficulty '{user_difficulty.get()}'") # Label above the input(s)
    make_questions() # Make / show all the questions on screen
    make_submit(validate_user_answers) # Add the submit button


# Call the functions for the starting difficulty choosing screen
def starting_difficulty_screen():
    make_label("Choose your starting difficulty") # Label above the input(s)
    make_difficulty_options() # Make / show all the difficulties the user can choose to start 
    make_submit(question_screen) # Add the submit button




# If the program starts
if __name__ == "__main__":
    starting_difficulty_screen() # Function to choose the starting difficulty
    window.mainloop()