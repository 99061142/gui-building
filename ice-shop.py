import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Make the window


# Item amount / prices
items = {
    "customer": {
        "scoop": {
            "price": 0.95,
            "amount": 0,
        },

        "cone": {
            "price": 1.25,
            "amount": 0,
        },

        "cup": {
            "price":  0.75,
            "amount": 0,
        },
        
        "whipped_cream": {
            "price": 0.5,
            "amount": 0,
        },
            
        "sprinkles": {
            "price": 0.3,
            "amount": 0,
        },

        "caramel_sauce": {
            "cone": {
                "price": 0.6,
                "amount": 0
            },

            "cup": {
                "price": 0.9,
                "amount": 0
            }
        }
    },

    "business": {
        "litre": {
            "price": 9.8,
            "amount": 0
        }
    }
}


user_role = tk.StringVar(value='customer') # Users role
scoops_litres_amount = tk.StringVar(value='1') # Amount of scoop(s)/litre(s)
scoop_litre = tk.StringVar() # Information if the user must choose the amount of scoop(s) or litre(s)
cone_cup = tk.StringVar(value="cone") # Users choice for a cone or a cup
label_text = tk.StringVar() # Text inside the label
want_receipt = tk.StringVar(value="no") # If the user wants the receipt

function_num = 0 # Index for the dictionary of the function information
must_ask_cone_cup = False # If the user must gets asked for a cone / cup
flavour_amounts = [] # Amount for the flavours



# Clear the window
def clear_window():
    # Clear the window
    for item in window.winfo_children():
        item.destroy()


# Make the question
def make_label():
    tk.Label(textvariable=label_text, font=('arial', 14)).grid(row=0, column=0, pady=('0', '10')) # Make the question and add it to the window    


# Update the label text
def update_label_text(text):
    label_text.set(text)
    make_label()


# Make the submit button
def make_submit(command):  
    tk.Button(text='submit', bg='gray', font=('arial', 10), command=command).grid(sticky='EW', columnspan=2, pady=('10', '0'))


# Make the input
def make_input(input:str, input_storage, array=None):
    if input == "radiobutton":
        # Make the options
        for role in array:
            ttk.Radiobutton(window, text=f"{role.capitalize()}", value=f"{role}", variable=input_storage).grid()
    
    elif input == "spinbox":
        if isinstance(array, tuple):
            for row, question in enumerate(array):
                question_row = row + 1

                answer = tk.StringVar()
                input_storage.append(answer)

                tk.Label(text=question, font=('arial', 14)).grid(row=question_row, column=0, sticky='w', pady=('0', '10'))
                tk.Spinbox(window, textvariable=answer, from_=0, to=float('inf')).grid(row=question_row, column=1, sticky='w') # Input
        else:
            tk.Spinbox(window, textvariable=input_storage, from_=1, to=float('inf')).grid(row=0, column=1, sticky='w') # Input

    elif input == "combobox":
        combobox = ttk.Combobox(window, textvariable=input_storage, state='readonly')
        combobox['values'] = array # All the options
        combobox.grid(row=0, column=1, sticky='w')


# Get the information what the user can buy
def validate_role():
    # Add the information what the user can buy
    scoop_litre_information = "scoop" if user_role.get() == "customer" else "litre"
    scoop_litre.set(scoop_litre_information)

    make_question() # Go to the next question


# Validate the amount for the scoop(s) / litre(s)
def validate_amount():
    global must_ask_cone_cup

    # Check if the user chose a number
    try:
        amount = int(scoops_litres_amount.get()) # Amount the user chose

    # If the user did not choose a number
    except ValueError:
        scoops_litres_amount.set(1) # Reset the amount the user wants to buy

    # If the user chose a number
    else:
        # Standard a cup
        if amount >= 4 and amount <= 8:
            cone_cup.set("cup")
        else:
            must_ask_cone_cup = True

        # If the user chose a number that is not a valid option
        if amount <= 0 or amount > 8:
            scoops_litres_amount.set(1) # Reset the amount the user wants to buy
        else:
            make_question() # Go to the next question


# Check if the user chose a flavour for every scoop / litre 
def validate_flavour():
    validation = True
    flavour_total_amount = 0
    max_amount = int(scoops_litres_amount.get())

    for flavour_amount in flavour_amounts:
        if not flavour_amount.get().isdigit():
            break
        else:
            flavour_total_amount += int(flavour_amount.get())
    
    else:
        if flavour_total_amount > max_amount:
            difference = flavour_total_amount - max_amount 

            message = f"You added {difference} {scoop_litre.get()}(s) too much"
        
        elif flavour_total_amount < max_amount:
            difference = max_amount - flavour_total_amount 

            message = f"You can add {difference} more {scoop_litre.get()}(s)"

        if flavour_total_amount != max_amount:
            label_text.set(message)

        else:
            make_question()


# Check if the user wants to see the receipt
def validate_ask_receipt():
    add_items()

    if want_receipt.get() == "yes":
        make_question() # Ask the same questions again
    else:
        clear_window()
        show_receipt() # Show the receipt to the user


# Make the question with the function information
def make_question(): 
    global function_num

    function_name = list( function_information.keys() )[function_num] # Get the key for the question

    # Get all the information to make the question
    question = function_information[function_name]['question']() # Question
    input_name = function_information[function_name]['input'] # Type of input
    stringvar = function_information[function_name]['stringvar'] # Storage for the answer of the user
    submit_function = function_information[function_name]['submit_function'] # Submit function


    clear_window() # Clear the previous question
    update_label_text(question) # Add the new question

    # Check if the user can choice between a few options
    try:
        input_array = function_information[function_name]['input_array']
    
    # If there is not a list with options
    except KeyError:
        make_input(input_name, stringvar) # Make the input to choice the option
    
    # If there is a list with options
    else:   
        make_input(input_name, stringvar, input_array) # Make the input to choice the option

    make_submit(submit_function) # Make the submit button

    # Go to the next question
    function_num += 1

    try:
        new_function_name = list( function_information.keys() )[function_num] # Check if there is another question after the question the user is in
    except IndexError:
        function_num = 0 # Reset the question index
    else:
        # If the user don't need to get asked for a cone or a cup
        if new_function_name == "cone_cup" and not must_ask_cone_cup:
            function_num += 1


# Add the items to the receipt dictionary
def add_items():
    amount = int(scoops_litres_amount.get())
    role = user_role.get()
    

    items[role][scoop_litre.get()]['amount'] += amount

    if cone_cup.get() and user_role.get() == "customer":
        items[role][cone_cup.get()]['amount'] += 1


# Show the bought items to the user
def show_receipt():
    role = user_role.get()

    receipt_price = 0


    tk.Label(text='---------["Papi Gelato"]---------', font=('arial', 14)).grid(pady=('5', '10')) # Receipt start

    # For every item that the user can buy
    for item, item_information in zip(items[role], items[role].values()):
        bought_item = False # If the user bought the item

        # Check if the user bought the item
        try:
            # Check with the role, if the user bought the item
            if item_information[cone_cup.get()]['amount'] > 0:
                bought_item = True    
        except KeyError:
            # Check without the role, if the user bought the item
            if item_information['amount'] > 0:
                bought_item = True

        # If the user bought the item
        if bought_item:
            # Get the information with the role of the user
            try: 
                item_price = item_information[cone_cup.get()]['price']
                item_amount = item_information[cone_cup.get()]['amount']
            
            # Get the information without the role of the user
            except KeyError:
                item_price = item_information['price']
                item_amount = item_information['amount']

            total_item_price = item_amount * item_price # Total price of the item
            receipt_price += total_item_price # Total receipt price without VAT


            item_price = "{:.2f}".format(item_price)
            total_item_price = "{:.2f}".format(total_item_price)

            tk.Label(text=f"{item}           {item_amount} * {item_price}   = €{total_item_price}", font=('arial', 14)).grid(pady=('0', '5')) # Show the item, amount, price and the total price for the item
    else:
        receipt_price = "{:.2f}".format(receipt_price)

        # Make the ending of the receipt
        tk.Label(text="                              ---------", font=('arial', 14)).grid(pady=('0', '5'))  
        tk.Label(text=f"Total                     = €{receipt_price}", font=('arial', 14)).grid() # Show the total price with VAT

        # If the users role is business
        if user_role.get() == "business":
            vat_price = receipt_price * 0.06
            vat_price = "{:.2f}".format(vat_price)

            tk.Label(text=f"VAT (9%)               = €{vat_price}", font=('arial', 14)).grid() # Show the VAT price




function_information = {
    "role": {
        "question": lambda: "Are you a customer or a business?",
        "input": "radiobutton",
        "input_array": ("customer", "business"),
        "submit_function": validate_role,
        "stringvar": user_role
    },

    "amount": {
        "question": lambda: f"How many {scoop_litre.get()}(s) do you want?",
        "input": "spinbox",
        "submit_function": validate_amount,
        "stringvar": scoops_litres_amount
    },

    "flavour": {
        "question": lambda: f"You can add {scoops_litres_amount.get()} more {scoop_litre.get()}(s)",
        "input": "spinbox",
        "input_array": ("Amount of strawberry", "Amount of chocolate", "Amount of vanilla"),
        "submit_function": validate_flavour,
        "stringvar": flavour_amounts
    },

    "cone_cup": {
        "question": lambda: f"Do you want the {scoops_litres_amount.get()} in a cup or a bucket?",
        "input": "combobox",
        "input_array": ("cone", "cup"),
        "submit_function": make_question,
        "stringvar": cone_cup
    },

    "ask_receipt": {
        "question": lambda: f"Do you want to buy more?",
        "input": "radiobutton",
        "input_array": ("yes", "no"),
        "submit_function": validate_ask_receipt,
        "stringvar": want_receipt
    }
}




# When the program starts
if __name__ == "__main__":
    make_question()
    window.mainloop() # Starts the window