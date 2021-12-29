import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint


window = tk.Tk() # Make the window

guessed_number = tk.StringVar()
score = tk.IntVar(value=0)
game_round = tk.IntVar(value=10)
number = tk.IntVar(value=randint(1, 1000))
guesses = tk.IntVar(value=1)


def difference_information(user_number):   
    # If the guessed number is 50 difference of the number
    if user_number - number.get() >= -50 and user_number - number.get() <= 50: 
        # If the guessed number is 20 difference of the number
        if user_number - number.get() >= -20 and user_number - number.get() <= 20:
            messagebox.showinfo(None, "U bent heel warm")
        else:
            messagebox.showinfo(None, "U bent warm")
    else:
        # If the number is higher than the guessed number
        if user_number < number.get():
            messagebox.showinfo(None, "hoger")
        
        # If the number is lower than the guessed number
        else:    
            messagebox.showinfo(None, "lager")


def check_guess():    
    user_number = guessed_number.get() # Guessed number
    guesses_amount = guesses.get() # Guessed amount

    # If the user typed a number
    if user_number.isdigit():
        user_number = int(user_number)

        guesses.set(guesses_amount + 1) # Add 1 try

        # If the guessed number was not the correct number
        if user_number != number.get():
            difference_information(user_number) # Give an message if the user must guess lower / higher

        # If the user guessed 10 times, or the user guessed the number correctly
        if guesses_amount == 10 or user_number == number.get():
            game_round.set(game_round.get() - 1) # Add 1 round
            reset_values() # Reset the values
    
        # If the user guessed the number correctly
        if user_number == number.get():
            score.set(score.get() + 1)

# Make the game screen
def game_screen():
    ttk.Entry(window, textvariable=guessed_number).pack() # Input
    tk.Button(text="Submit", bg='gray', font=('arial', 10), command=check_guess).pack(side='left', expand=True, fill='both') # Submit the input
    tk.Button(text="Stop", bg='gray', font=('arial', 10), command=exit).pack(side='right', expand=True, fill='both') # Stop the program


# Reset the values
def reset_values():
    messagebox.showinfo(None, f"Het nummer dat geraden moest worden is veranderd. U heeft nog {game_round.get()} rondes te gaan")
    number.set(randint(1, 1000)) # Number that need to be guessed
    guesses.set(1) # Amount of guesses the user has done




# When the program starts
if __name__ == "__main__":
    game_screen() # Make the game screen
    window.mainloop() # Show the window