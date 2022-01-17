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

        "max_mistakes": 0,
        "user_mistakes": 0,
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

        "max_mistakes": 0,
        "user_mistakes": 0,
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

        "max_mistakes": 1,
        "user_mistakes": 0,
        "questions_made": False
    }
}


user_difficulty = tk.StringVar(value="easy") # Which difficulty the user is on
highest_difficulty = tk.StringVar()
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

    # For every question
    for user_answer in user_sum_answers:
        # Check if it is a number
        try:
            int(user_answer.get()) 

        # If it is not a number
        except ValueError:
            user_answer.set(0) # Reset the value of the input
            error_made = True 
    
    # If every answer is validated
    else:
        # If all the answers of the user were numbers
        if not error_made:
            error_made = False
            calculate_user_answer() # Calculate the mistakes of the user


# Check if the user gave the good answers on the questions
def calculate_user_answer():
    mistakes_made = 0

    difficulty = user_difficulty.get() # Difficulty the user is on

    sum_information_route = sum_information[difficulty] # Route to the users difficulty sum information

    # Get all the answers
    questions = sum_information_route['questions'] # All the questions
    answers = [eval(question) for question in questions] # All the answers on the questions

    user_answers = [int( user_answer.get() ) for user_answer in user_sum_answers] # All the answers of the user

    # For every question
    for user_answer, answer in zip(user_answers, answers):
        if user_answer != answer:
            mistakes_made += 1
        
    else:
        sum_information_route['user_mistakes'] = mistakes_made
        sum_information_route['questions_made'] = True

        get_new_difficulty(difficulty, sum_information_route, mistakes_made)


# Get the new difficulty, or show the endscreen if the user is done with the questions
def get_new_difficulty(difficulty:str, sum_information_route:dict, mistakes_made:int):
    difficulties = list( sum_information.keys() ) # ALl the difficulties

    end_score = "won" if mistakes_made <= sum_information_route['max_mistakes'] else "lost" # Get if the user lost or won
    add_index_number = 1 if end_score == "won" else -1 # Increase or decrease the index of the difficulty out of all the difficulty options
    
    must_show_endscreen = False # If the user lost or won the game
    
    # If the user did not lose the easy questions
    if difficulty != "easy" or difficulty == "easy" and end_score == "won":
        # Check if the user did not win the last difficulty
        try:
            # Get the new difficulty
            next_difficulty_index = difficulties.index(difficulty) + add_index_number
            next_difficulty = difficulties[next_difficulty_index]

        # If the user won the hardest difficulty
        except IndexError:
            must_show_endscreen = True # If the user must see the end screen

    # If the user lost the easy difficulty
    else:
        must_show_endscreen = True # If the user must see the end screen

    # If the user lost the lowest difficulty or won the highest difficulty
    if must_show_endscreen:
        get_new_gamemode(must_show_endscreen, end_score) # Get the new questions, or show the end screen
    else:
        get_new_gamemode(must_show_endscreen, end_score, next_difficulty) # Get the new questions, or show the end screen


# Check if the user must see the new questions, or that the user is done with the game
def get_new_gamemode(must_show_endscreen:bool, end_score:str, next_difficulty:str=None):
    difficulty = user_difficulty.get() # The difficulty the user is on

    # If the user did not  lose the lowest difficulty and did not win the highest difficulty
    if next_difficulty != None:
        next_difficulty_user_mistakes = sum_information[next_difficulty]['user_mistakes'] # Mistakes the user made on the next difficulty
        next_difficulty_max_mistakes = sum_information[next_difficulty]['max_mistakes'] # Max mistakes the user could make on the next difficulty
        next_difficulty_questions_made = sum_information[next_difficulty]['questions_made'] # If the user made the next difficulty questions

        if next_difficulty_questions_made:
            if next_difficulty_user_mistakes <= next_difficulty_max_mistakes:
                difficulty = next_difficulty # Update the difficulty to the next difficulty

            must_show_endscreen = True # If the user must see the end screen


    if must_show_endscreen: 
        highest_difficulty.set(difficulty) # Update the highest difficulty
        end_screen(end_score) # Show if the user lost or won
    else:
        user_difficulty.set(next_difficulty) # Update the difficulty
        question_screen() # Show the new question screen


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


# Endscreen if the game is over
def end_screen(end_score:str):
    clear_window() # Clear everything on the window

    make_label(f"You {end_score} the game, your highest difficulty was '{highest_difficulty.get()}'") # Label that show the users end score


# Call the functions for the question screen
def question_screen():  
    clear_window() # Clear everything on the window
    user_sum_answers.clear() # Delete everything in the list

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