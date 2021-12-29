import tkinter as tk
from tkinter.messagebox import showinfo
from random import randint


window = tk.Tk() # Make the window

guessed_number = tk.StringVar()
score = tk.IntVar(value=0)
game_round = tk.IntVar(value=20)
number = tk.IntVar(value=randint(1, 1000))
guesses = tk.IntVar(value=1)


# Clear the window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Show if the user is close to the number
def difference_information(user_number):   
    # If the guessed number is 50 difference of the number
    if user_number - number.get() >= -50 and user_number - number.get() <= 50: 
        # If the guessed number is 20 difference of the number
        if user_number - number.get() >= -20 and user_number - number.get() <= 20:
            showinfo(None, "U bent heel warm")
        else:
            showinfo(None, "U bent warm")
    else:
        # If the number is higher than the guessed number
        if user_number < number.get():
            showinfo(None, "hoger")
        
        # If the number is lower than the guessed number
        else:    
            showinfo(None, "lager")


# Ask if the user wants to guess another number
def next_round(guessed_correctly):
    clear_window() # Clear the window

    # If the user guessed the number correctly
    if guessed_correctly:
        score.set(score.get() + 1) # Add 1 points to the score


    # If the user has rounds left
    if game_round.get() > 0:
        if guessed_correctly:
            message = "U heeft het nummer goed geraden"
        else:
            message = f"U heeft het nummer fout geraden, het nummer was {number.get()}"

        tk.Label(text=f"{message}. Wilt u nog een nummer raden?" , font=('arial', 14)).pack(fill='both')
        tk.Button(text="Yes", bg='gray', font=('arial', 10), command=reset_values).pack(side='left', expand=True, fill='both') # Go to the next random number
        tk.Button(text="No", bg='gray', font=('arial', 10), command=exit).pack(side='right', expand=True, fill='both') # Stop the program
    else:
        end_screen() # Show the end screen


def check_guess():    
    user_number = guessed_number.get() # Guessed number
    guesses_amount = guesses.get() # Guessed amount

    # If the user typed a number
    if user_number.isdigit():
        user_number = int(user_number)

        guesses.set(guesses_amount + 1) # Add 1 try

        # If the guessed number was not the correct number
        if user_number != number.get() and guesses_amount < 10:
            difference_information(user_number) # Give an message if the user must guess lower / higher

        # If the user guessed 10 times, or the user guessed the number correctly
        else:
            game_round.set(game_round.get() - 1) # Add 1 round

            guessed_correctly = True if user_number == number.get() else False # Check if the user guessed the number correctly

            next_round(guessed_correctly) # Ask if the user wants to guess another number


# Screen if the game is over
def end_screen():
    tk.Label(text=f"U heeft in totaal {score.get()} nummer(s) geraden." , font=('arial', 14)).pack(fill='both')


# Make the game screen
def game_screen():
    tk.Entry(window, textvariable=guessed_number).pack() # Input
    tk.Button(text="Submit", bg='gray', font=('arial', 10), command=check_guess).pack(side='left', expand=True, fill='both') # Submit the input
    tk.Button(text="Stop", bg='gray', font=('arial', 10), command=exit).pack(side='right', expand=True, fill='both') # Stop the program


# Reset the values
def reset_values():
    showinfo(None, f"Het nummer dat geraden moest worden is veranderd. U heeft nog {game_round.get()} rondes te gaan")
    number.set(randint(1, 1000)) # Number that need to be guessed
    guesses.set(1) # Amount of guesses the user has done
    guessed_number.set('') # Users guess

    clear_window() # Clear the window
    game_screen() # Show the game screen



# When the program starts
if __name__ == "__main__":
    game_screen() # Make the game screen
    window.mainloop() # Show the window