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


user_role = tk.StringVar(value='particulier')


# Get the role
def ask_role():
    roles = ("particulier", "zakelijk") # All the roles

    # Make the question
    roles_options = " of ".join(roles)
    question = f"bent u {roles_options}"

    tk.Label(text=question, font=('arial', 14, 'bold')).pack(fill='x') # Title

    # Make the options
    for role in roles:
        ttk.Radiobutton(window, text=f"{role.capitalize()}", value=f"{role}", variable=user_role).pack() # Options
    
    # Add the submit button when all the options are made
    else:
        tk.Button(text="Verder", bg='gray', font=('arial', 10), command=role_icing).pack(side='left', expand=True, fill='x') # Submit button


def role_icing():
    if user_role.get() == "particulier":
        get_scoops()
    else:
        get_litres()


def get_scoops():
    pass


def get_litres():
    pass


def main():
    print("Welkom bij Papi Gelato") # Welcomes the user
    ask_role()




# When the program starts
if __name__ == "__main__":
    main()
    window.mainloop()