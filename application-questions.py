import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window

# Array with all the questions that gets asked
all_questions = {
    "work": {
        "Hoeveel jaar praktijkervaring heeft u met dieren-dressuur (alleen nummer(s))": 4,
        "Hoeveel jaar praktijkervaring heeft u met jongleren (alleen nummer(s))": 5,
        "Hoeveel jaar praktijkervaring heeft u met acrobatiek (alleen nummer(s))": 3,
    },

    "person_information": {
        "Wat is uw lengte (in cm / alleen nummer(s))": 150,
        "wat is uw lichaamsgewicht": 90
    },

    "lifestyle": {
        "Bent u in het bezit van een Diploma MBO-4 ondernemen": "ja",
        "Bent u in het bezit van een geldig Vrachtwagen rijbewijs": "ja",
        "Bent u in het bezit van een hoge hoed": "ja",
        "Wat is uw lichaamsgewicht": "ja",
        "Heeft u het Certificaat 'Overleven met gevaarlijk personeel'": "ja"
    },

    "useless": {
        "Heeft u huisdieren": '',
        "Bent u in het bezit van een motor rijbewijs": '',
        "Wou u deze baan altijd al hebben": '',
        "Heeft u een kind": ''
    }
}

# Questions for the gender of the user
gender_questions = {
    "male": {
        "Is uw snor breder dan 10 cm": "ja",
    },

    "female": {
        "Draagt u rood krulhaar langer dan 20 cm": "ja"
    }
}

gender = tk.StringVar(value="Male") # Users gender

answers = {} # All the answers the user gave


# Clear the window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Show the user if he is valid for the job
def show_validation(validation):
    clear_window() # Clear the window

    # Show if the application is approved
    user_validation = "goedgekeurd" if validation else "niet goedgekeurd"

    tk.Label(text=f"Uw applicatie is {user_validation}", font=('arial', 14)).pack(fill='both')


# Check if the user is valid for the job
def check_validation(): 
    validation = True

    work_answers = [] # List with the correct answers (1 must be true)

    # Check every answer the user gave
    for key in all_questions:     
        for good_answer, user_answer in zip(all_questions[key].values(), answers[key].values()):
            user_answer = user_answer.get()
            
            # Check if the user answered 1 question correctly from the 'work' questions
            if key == "work":
                if user_answer.isdigit():
                    possibility_validation = False if int(user_answer) < good_answer else True
                    work_answers.append(possibility_validation)

            # If the questions are not about 'work' and not 'useless'
            else:
                # If the correct answer is a number
                if isinstance(good_answer, int):
                    if user_answer.isdigit():   
                        # If the user answered a lower number than the correct number
                        if int(user_answer) < good_answer:
                            validation = False
                
                # If the correct answer is a text
                else:   
                    # If the user did not ansswer the same text as the correct answer
                    if user_answer != good_answer:
                        validation = False
    
    # When all the questions are checked
    else:  
        # If the user correctly answered 1 of the 'possibility' questions 
        if work_answers.count(True) < 1:
            validation = False

        show_validation(validation) # Show the user if he passed the application


# Show all the questions 
def show_questions():
    clear_window() # Clear the previous window

    row = 0 # Starting row value

    # loop through every question
    for key in all_questions:
        for question in all_questions[key]:
            answer = tk.StringVar() 

            tk.Label(text=f"{question}?", font=('arial', 14)).grid(row=row, column=0) # Question

            # Input
            if isinstance(all_questions[key][question], str):
                question_input = ttk.Combobox(window, text='t', width=8, textvariable=answer)
                question_input['values'] = ("ja", "nee") # Add the options
                question_input['state'] = "readonly" # User must choose a value that is a valid option
            else:
                question_input = tk.Spinbox(window, from_=0, to=100, textvariable=answer)

            question_input.grid(row=row, column=1)

            row += 1 # Go to the next row
            
            # Add the question + answer to the user answers dictionary
            try: 
                answers[key]
            except KeyError:
                answers[key] = {}
            finally:
                if key != "useless":
                    answers[key][question] = answer
    
    # When every question is made
    else:
        tk.Button(text="Submit", bg='gray', font=('arial', 10), command=check_validation).grid(columnspan=2, sticky='nsew') # Button to submit the answers


# Add the gender question(s) to the questions
def add_gender():   
    user_gender = gender.get().lower() # Get the users gender 

    all_questions['gender_questions'] = gender_questions[user_gender] # Add the gender question(s) to the questions


    show_questions() # Show all the questions


# Ask the users gender
def ask_gender():
    tk.Label(text="Bent u een man of een vrouw?" , font=('arial', 14)).grid(row=0, column=0) # Question

    # Input
    gender_input = ttk.Combobox(window, textvariable=gender, width=8)
    gender_input['values'] = ("Male", "Female") # Add the options
    gender_input['state'] = "readonly" # User must choose a value that is a valid option
    gender_input.grid(row=0, column=1)

    tk.Button(text="Submit", bg='gray', font=('arial', 10), command=add_gender).grid(columnspan=2, sticky='nsew') # Button to submit the answer




# When the program starts
if __name__ == "__main__":
    ask_gender()
    window.mainloop()