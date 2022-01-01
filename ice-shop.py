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
    validation = True

    # Check every answer
    for flavour in flavour_answers:
        # If the answer is not a valid flavour
        if flavour.get() not in flavours: 
            validation = False

    else:
        # If the user chose a valid flavour for every scoop/litr
        if validation:
            # If the user is a individual
            if user_role.get() == "particulier":
                ask_toppings()
            
            # If the user is from a business
            else:
                make_receipt()


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

    total_amount = int(scoops_litres.get()) # Users input
    number = 1

    while number <= total_amount:
        answer = tk.StringVar()
        flavour_answers.append(answer)

        question = "Welke smaak wilt u voor "
        question += f"bolletje nummer {number}" if user_role.get() == "particulier" else f"liter nummer {number}"

        tk.Label(text=question, font=('arial', 14)).grid(row=number, column=0) # Question

        # Input
        question_input = ttk.Combobox(window, textvariable=answer)
        question_input['values'] = flavours # Flavour options
        question_input['state'] = "readonly" # User must choose a value that is a valid option
        question_input.grid(row=number, column=1)

        number += 1
    
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