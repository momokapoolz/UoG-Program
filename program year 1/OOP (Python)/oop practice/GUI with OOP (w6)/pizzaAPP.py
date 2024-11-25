import tkinter as tk

import pizzaOOP as pz


def respond():
    pizza_type = chosen.get()
    pizza_price = pizzas[pizza_type]
    description = pizza_type
    extras_description = ""
    for extra in extras:
        if extra_chosen[extra].get():
            if extras_description == "":
                extras_description += f" with extra {extra}"
            else:
                extras_description += f", {extra}"
            pizza_price += extras[extra]
    description += extras_description
    print(f"Pizza chosen is {description}")
    txt_output.set(f"Pizza price is £{pizza_price:.2f}")


def add_to_basket():
    pizza_type = chosen.get()
    pizza_price = pizzas[pizza_type]
    chosen_pizza = pz.Pizza(pizza_type, pizza_price)
    for extra in extras:
        if extra_chosen[extra].get():
            extra_price = extras[extra]
            chosen_pizza.add_extra(extra, extra_price)
    basket.append(chosen_pizza)
    txt_basket["state"] = "normal"
    txt_basket.delete("1.0", tk.END)
    contents = ""
    total_cost = 0
    for chosen_pizza in basket:
        contents += chosen_pizza.get_description() + "\n"
        total_cost += chosen_pizza.price
    txt_basket.insert(1.0, contents)
    txt_basket["state"] = "disabled"
    basket_output.set(f"Total cost is £{total_cost:.2f}")


def empty_basket():
    #clear basket list
    basket.clear()

    #clear text box basket
    txt_basket["state"] = "normal"
    txt_basket.delete("1.0", tk.END)
    txt_basket["state"] = "disable"

    #clear total cost
    total_cost = 0
    basket_output.set(f"Total cost is £{total_cost:.2f}")

    #clear check box
    for chk in chk_extraa:
        chk.deselect()
    

    


window = tk.Tk()
window.geometry("500x600")
window.title("Python pizzas")

basket = []

row_counter = 0

lbl0 = tk.Label(window, text="Pizzas", font=("Arial Bold", 20))
lbl0.grid(column=0, row=row_counter, sticky="W")
row_counter += 1

chosen = tk.StringVar(window)
chosen.set("margherita")

pizzas = {"margherita": 6.0, "napoletana": 7.0, "marinara": 7.5}

for pizza in pizzas:
    rad = tk.Radiobutton(window, text=f"{pizza} - £{pizzas[pizza]:.2f}", value=pizza, variable=chosen, command=respond)
    rad.grid(column=0, row=row_counter, sticky="W")
    row_counter += 1

lbl1 = tk.Label(window, text="Extras", font=("Arial Bold", 20))
lbl1.grid(column=0, row=row_counter, sticky="W")
row_counter += 1

extras = {"mushrooms": 0.5, "cheese": 1.0, "anchovies": 1.5, "sausage": 1.8}

#check box ae
extra_chosen = {}
chk_extraa = []

for extra in extras:
    extra_chosen[extra] = tk.BooleanVar(window)
    chk = tk.Checkbutton(window, text=f"{extra} - £{extras[extra]:.2f}", var=extra_chosen[extra], command=respond)
    chk.grid(column=0, row=row_counter, sticky="W")
    row_counter += 1
    chk_extraa.append(chk)

txt_output = tk.StringVar(window)

txt = tk.Entry(window, width=25, textvariable=txt_output, state="readonly")
txt.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1

add_button = tk.Button(window, text="Add to basket", command=add_to_basket)
add_button.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)

empty_basket_button = tk.Button(window, text="Empty basket", command=empty_basket)
empty_basket_button.grid(column=1, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1

lbl1 = tk.Label(window, text="Basket", font=("Arial Bold", 20))
lbl1.grid(column=0, row=row_counter, sticky="W")
row_counter += 1

txt_basket = tk.Text(window, width=60, height=10, state="disabled")
txt_basket.grid(column=0, row=row_counter, columnspan=2, sticky="W", padx=5, pady=5)
row_counter += 1

basket_output = tk.StringVar(window)

txt_totalCost = tk.Entry(window, width=25, textvariable=basket_output, state="readonly")
txt_totalCost.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1

exit_button = tk.Button(window, text="Exit", command=exit)
exit_button.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1





respond()

window.mainloop()