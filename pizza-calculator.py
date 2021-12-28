import tkinter as tk
from tkinter import ttk
from time import sleep

window = tk.Tk() # Makes the window

chosen_size = tk.StringVar()
chosen_amount = tk.StringVar()

pizza_information = {}
pizza_prices = {"small": 4, "medium": 6, "large": 11}

# Clear the window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Reset the values
def reset_values():
    chosen_size.set('') # Reset the value for the pizza size
    chosen_amount.set('') # Reset the value for the pizza amount


# Check if the user chose a number
def validate_amount():  
    # If the user chose a number
    if chosen_amount.get().isdigit():
        if int(chosen_amount.get()) > 0:
            clear_window() # Clear the window
            ask_receipt() # Go to the screen to ask if the user wants to show the receipt


# Check if the user chose a size for the pizza
def validate_size():
    # If the user chose a size
    if chosen_size.get():
        clear_window() # Clear the window
        pizza_amount() # Go to the screen to ask the amount


# If the user clicked 1 of the buttons of the questions to see the receipt
def wants_receipt(answer):
    clear_window() # Clear the window
    add_pizza() # Add the pizza to the receipt
    reset_values() # Reset the values the user chose

    # If the user wants to see the receipt
    if answer == "yes":
        receipt() # Show the receipt
    
    # If the user wants to buy more pizza's
    else:
        ask_size() # Ask the questions again


# Add the pizza to the dictionary
def add_pizza():
    size = chosen_size.get() # Pizza size
    amount = int(chosen_amount.get()) # Pizza amount

    # Add the pizza and the amount to the dictionary
    try:
        pizza_information[size] += amount
    except KeyError:
        pizza_information[size] =  amount


# Shows the receipt
def receipt():
    total_price = 0

    # Start of the receipt
    tk.Label(text="RECEIPT", font=("arial", 18, "bold")).pack(fill='y') 
    tk.Label(text="--------------------------------------", font=("arial", 16)).pack(fill='y') 

    # For every pizza that is bought
    for pizza, amount in pizza_information.items():
        pizza_price = pizza_prices[pizza] # Pizza price
        pizza_total_price = pizza_price * amount # Total price for all the pizza's with that size
        total_price += pizza_total_price # Total price for all the pizza's

        tk.Label(text=f"{pizza} pizza = {pizza_prices[pizza]} * {amount} = {pizza_total_price} euro", font=("arial", 16)).pack(fill='y') # Show the information about the pizza
    else:
        tk.Label(text="--------------------------------------", font=("arial", 16)).pack(fill='y') # End of the receipt
        tk.Label(text=f"totaal: {total_price} euro", font=("arial", 16)).pack(fill='y') # Total price


# Ask if the user wants to show the receipt
def ask_receipt():
    tk.Button(text="Yes", bg='gray', font=('arial', 10), command= lambda: wants_receipt('yes')).pack(side='left', expand=True, fill='both') # Button to submit the answer
    tk.Button(text="No", bg='gray', font=('arial', 10), command= lambda: wants_receipt('no')).pack(side='right', expand=True, fill='both') # Button to submit the answer


# Get the amount of the pizza
def pizza_amount():
    tk.Label(text=f"Kies het aantal {chosen_size.get()} pizza's:" , font=('arial', 14)).grid(row=0, column=0)
    tk.Entry(window, textvariable=chosen_amount).grid(row=0, column=1)
    tk.Button(text="Submit", bg='gray', font=('arial', 10), command=validate_amount).grid(columnspan=2, sticky='nsew') # Button to submit the answer


# Get the size of the pizza
def ask_size():
    sizes = ["small", "medium", "large"] # Valid sizes
    sizes_str = ', '.join([f"'{size}'" for size in sizes]) # Show all the sizes

    tk.Label(text=f"Welke grootte pizza wilt u hebben?, u heeft keuze tussen {sizes_str}", font=('arial', 14, 'bold')).pack(fill='x')

    for size in sizes:
        ttk.Radiobutton(window, text=f"{size.capitalize()}", value=f"{size}", variable=chosen_size).pack()
    else:
        tk.Button(text="Submit", bg='gray', font=('arial', 10), command=validate_size).pack(fill='both') # Button to submit the answer




# When the program starts
if __name__ == "__main__":
    ask_size()
    window.mainloop() # Shows the window