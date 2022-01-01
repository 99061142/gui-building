import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Item amount / prices
items = {
    "bolletje": {
        "price": 0.95,
        "amount": 0,
    },

    "liter": {
        "price": 9.8,
        "amount": 0
    },

    "hoorntje": {
        "price": 1.25,
        "amount": 0,
    },

    "bakje": {
        "price":  0.75,
        "amount": 0,
    },
}


# Topping amounts / prices
toppings = {    
    "geen": {
        "price": 0,
        "amount": 0
    },

    "slagroom": {
        "price": 0.5,
        "amount": 0,
    },
    
    "sprinkels": {
        "price": 0.3,
        "amount": 0,
    },

    "caramel_saus": {
        "hoorntje": {
            "price": 0.6,
            "amount": 0
        },

        "bakje": {
            "price": 0.9,
            "amount": 0
        },
    
        "amount": 0,
    }
}


flavours = ("Aardbei", "Chocolada", "Vanille") # Flavours the user can buy
flavour_answers = [] # Every flavour the user bought


user_role = tk.StringVar(value='particulier') # Users role
scoops_litres = tk.StringVar(value=1) # Amount of scoop(s)/litre(s)
amount_left_str = tk.StringVar()


# Clear the window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Validate if the user chose a number higher than 0 
def validate_amount():
    amount = scoops_litres.get() # Users input

    # IF the user chose a number higher than 0
    if amount.isdigit() and amount[0] != '0':
        ask_flavour() # Ask the flavour per scoop / litre
    else:
        scoops_litres.set(1) # Reset the value for the amount the user wants to buy


# Check if the user chose a valid flavour for every scoop/litre
def validate_flavours():
    total_amount = 0

    scoops_litres_amount = int(scoops_litres.get()) # Total scoop(s) / litre(s)

    question_information = "bolletje(s)" if user_role.get() == "particulier" else "liter(s)" # Information if the user wants to buy scoops or litres

    # Check every flavour amount the user chose
    for flavour_amount in flavour_answers:
        flavour_amount = int(flavour_amount.get()) 

        total_amount += flavour_amount # Add the amount to the total amount
    else:
        # When the user can add more scoop(s) / litre(s) to a flavour
        if scoops_litres_amount > total_amount:
            amount_left_str.set(f"U kan nog {scoops_litres_amount - total_amount} {question_information} toevoegen aan een smaak")
        
        # When the user did add more scoop(s) / litre(s) than the max amount
        elif scoops_litres_amount < total_amount:
            amount_left_str.set(f"U heeft {total_amount - scoops_litres_amount} {question_information} teveel toegevoegd aan een smaak")


# Get the role
def ask_role():
    roles = ("particulier", "zakelijk") # All the roles

    # Make the question
    roles_options = " of ".join(roles)
    question = f"bent u {roles_options}"

    tk.Label(text='Welkom bij Papi Gelato', font=('arial', 18, 'bold')).pack(fill='x') # Welcomes the user
    tk.Label(text=question, font=('arial', 14, 'bold')).pack(fill='x') # Question

    # Make the options
    for role in roles:
        ttk.Radiobutton(window, text=f"{role.capitalize()}", value=f"{role}", variable=user_role).pack() # Options
    
    # Add the submit button when all the options are made
    else:
        tk.Button(text="Verder", bg='gray', font=('arial', 10), command=get_scoops).pack(side='left', expand=True, fill='x') # Submit button


# Ask how many scoops / litres the user wants
def get_scoops():
    clear_window() # Clear the previous question(s)

    question = "liter(s) ijs" if user_role.get() == "zakelijk" else "bolletjes" # Information what the user must buy

    tk.Label(text=f"Kies het aantal {question} wat u wilt kopen (voorbeeld: 1, 2, 3):", font=('arial', 14)).grid(row=0, column=0) # Question
    tk.Spinbox(window, textvariable=scoops_litres, from_=1, to=float('inf')).grid(row=0, column=1) # Input
    tk.Button(text="Submit", font=('arial', 10), bg='gray', command=validate_amount).grid(columnspan=2, sticky='nsew') # Button to submit the answer


# Ask the flavour per scoop / litre
def ask_flavour():
    clear_window()

    total_amount = int(scoops_litres.get()) # Chosen amount for scoop(s) / litre(s)

    # Show the user how many scoop(s)/litre(s) he can add to the flavours
    question_information = "bolletjes" if user_role.get() == "particulier" else "liters"
    amount_left_str.set(f"U kan nog {total_amount} {question_information} toevoegen aan een smaak")
    tk.Label(textvariable=amount_left_str, font=('arial', 14)).grid(row=0, column=0)

    # For every flavour option
    for row, flavour in enumerate(flavours):
        row += 1

        answer = tk.StringVar()
        flavour_answers.append(answer)
    
        tk.Label(text=f"Hoeveel {question_information} wilt u met de smaak {flavour}", font=('arial', 14)).grid(row=row, column=0) # Question
        tk.Spinbox(window, textvariable=answer, from_=0, to=float('inf')).grid(row=row, column=1) # Input
    
    # When every input is made
    else:
        tk.Button(text="Submit", font=('arial', 10), bg='gray', command=validate_flavours).grid(columnspan=2, sticky='nsew') # Button to submit the answer


# Ask which topping the user wants to buy per scoop
def ask_toppings():
    pass


# Add the items to the receipt
def make_receipt():
    pass




# When the program starts
if __name__ == "__main__":
    ask_role()
    window.mainloop()