import tkinter as tk
from tkinter import ttk
from time import sleep

window = tk.Tk() # Makes the window

chosen_size = tk.StringVar()
chosen_amount = tk.StringVar()


# Clear the window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Check if the user chose a number
def validate_amount():  
    # If the user chose a number
    if chosen_amount.get().isdigit():
        clear_window() # Clear the window
        ask_receipt() # Go to the screen to ask if the user wants to show the receipt


# Check if the user chose a size for the pizza
def validate_size():
    # If the user chose a size
    if chosen_size.get():
        clear_window() # Clear the window
        pizza_amount() # Go to the screen to ask the amount


# Ask if the user wants to show the receipt
def ask_receipt():
    pass


# Get the amount of the pizza
def pizza_amount():
    tk.Label(text=f"Kies het aantal {chosen_size.get()} pizza's:" , font=('arial', 14)).grid(row=0, column=0)
    tk.Entry(window, textvariable=chosen_amount).grid(row=0, column=1)
    tk.Button(text="Submit", bg='gray', font=('arial', 10), command=validate_amount).grid(columnspan=2, sticky="nsew") # Button to submit the answer


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