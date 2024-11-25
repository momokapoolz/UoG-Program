from tkinter import *

# Dictionary containing the fruit prices
fruit_prices = {
    'Apple': 0.5,
    'Banana': 0.25,
    'Orange': 0.3,
    'Peach': 0.6,
    'Watermelon': 0.5
}

fruit_var = ['Apple', 'Banana', 'Orange', 'Peach', 'Watermelon'] 


def cb_fruits_selected(*args):
    # Retrieve the selected fruit from the variable
    selected_fruit = fruit_var.get()

    # Get the price of the selected fruit from the dictionary
    fruit_price = fruit_prices[selected_fruit]

    # Update the price label with the selected fruit's price
    lbl_price = fruit_price.config(text=f"Price: ${fruit_price:.2f}")
    return lbl_price


def btn_calculate_clicked():
    # Retrieve the selected fruit and quantity from the respective widgets
    selected_fruit =  # TODO
    quantity = int(txt_quantity.get())

    # Calculate the total cost by multiplying the fruit price by the quantity
    total_cost =  # TODO

    # Update the total cost label with the calculated value
    total_cost_label.config(  # TODO)

        # Create the main window
        window=Tk()
    window.title("Fruit Ordering System")

    # Create a label to display fruit selection instructions
    fruit_label = Label(window, text="Select a fruit:")
    fruit_label.grid(row=0, column=0, sticky=W)

    # Create a variable to hold the selected fruit
    fruit_var = StringVar(window)
    fruit_var.set('Apple')  # Set a default fruit

    # Create a dropdown menu for fruit selection
    cb_fruits = OptionMenu(window,  # Parent widget
                           fruit_var,  # Variable to hold the selected fruit
                           *fruit_prices.keys(),  # List of fruits
                           command=cb_fruits_selected)  # Function to call when a fruit is selected
    cb_fruits.grid(row=0, column=1, sticky=W)

    # Create a label to display the fruit price
    lbl_price = Label(window, text="Price: $0.00")
    lbl_price.grid(row=0, column=2, sticky=W)

    # Create a label to display quantity instructions
    lbl_quantity = Label(window, text="Enter quantity:")
    lbl_quantity.grid(  # TODO)

        # Create an entry widget for quantity input
        txt_quantity=Entry(window)
    txt_quantity.grid(  # TODO)

        # Create a button to trigger the calculation
        btn_calculate=Button(window, text="Calculate Total", command=btn_calculate_clicked)
    btn_calculate.grid(row=1, column=2)

    # Create a label to display the total cost
    total_cost_label =  # TODO
    total_cost_label.grid(  # TODO)

        # Start the Tkinter event loop
        window.mainloop()