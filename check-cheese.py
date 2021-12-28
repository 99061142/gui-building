import tkinter as tk

window = tk.Tk() # Makes the window


question = tk.StringVar(value="Is de kaas geel") # Starting question
answer = tk.StringVar()

previous_question = tk.StringVar()
previous_answer = tk.StringVar()

end_cheese = tk.StringVar()
question_done = tk.BooleanVar()


# Clear the whole window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()



# Show the end cheese to the user
def show_end_cheese():
    clear_window() # Clear the window
    tk.Label(textvariable=end_cheese, font=('arial', 15, 'bold')).pack(fill='both') # Show the end cheese



def get_end_cheese():
    question_str = question.get()
    answer_str = answer.get()

    # Get the end cheese with the last question + input of the user

    if question_str == "Is de kaas belachelijk duur":
        if answer_str == "ja":
            end_cheese_str = "Emmenthaler"
        else:
            end_cheese_str = "Leerdammer"


    elif question_str == "Is de kaas hard als steen":
        if answer_str == "ja":
            end_cheese_str = "Pammigiano Reggiano"
        else:
            end_cheese_str = "Goudse kaas"



    elif question_str == "Heeft de kaas een korst":
        if previous_question.get() == "Heeft de kaas blauwe schimmels" and previous_answer.get() == "ja":
            if answer_str == "ja":
                end_cheese_str = "Bleu de Rochbaron"
            else:
                end_cheese_str = "Foumme d'Ambert"
        else:
            if answer_str == "ja":
                end_cheese_str = "Camembert"
            else:
                end_cheese_str = "Mozzarella"

    end_cheese.set(end_cheese_str) # Set the end cheese


def get_new_question():
    question_bool_done = False

    question_str = question.get()
    answer_str = answer.get()

    # Make the new questions

    if question_str == "Is de kaas geel":
        if answer_str == "ja":
            question_str = "zitten er gaten in"
        else:
            question_str = "Heeft de kaas blauwe schimmels"


    elif question_str == "zitten er gaten in":
        if answer_str == "ja":
            question_str = "Is de kaas belachelijk duur"
            question_bool_done = True
        else:
            question_str = "Is de kaas hard als steen"
            question_bool_done = True


    elif question_str == "Heeft de kaas blauwe schimmels":
        previous_question.set(question_str) # Set the previous question to this question
        previous_answer.set(answer_str) # Set the previous answer to the answer the user gave this question


        question_str = "Heeft de kaas een korst"
        question_bool_done = True


    question.set(question_str) # Update the question
    question_done.set(question_bool_done) # If the questions are over


# Update the question / show the question when it is done
def get_new_info():
    # When the questions are over
    if question_done.get():
        get_end_cheese() # Get the end cheese with the answers the user gave
        show_end_cheese() # Show the end cheese to the user
    
    # When there are more question
    else:
        get_new_question() # Update the question
        set_question() # Change the question


# Make / change the label + input for the question
def set_question():
    chosen_word = tk.StringVar()
    tk.Label(window, textvariable=question, font=('arial', 12)).grid(row=1, column=0) # Label for the question
    tk.Entry(window, textvariable=answer, width=35).grid(row=1, column=1) # Input for the question


# Show the question
def main():
    tk.Label(text="Als u niks invult, of niet 'ja' of 'nee', wordt het antwoord automatisch 'nee'", font=('arial', 15, 'bold')).grid(columnspan=2) # Information about the input

    set_question() # Make the starting question

    tk.Button(text="Submit", font=('arial', 10), command=get_new_info).grid(columnspan=2) # Button to submit the answer




# When the program starts
if __name__ == "__main__":
    main() # Show the first question
    window.mainloop() # Starts the window