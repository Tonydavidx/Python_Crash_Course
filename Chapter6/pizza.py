pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','tomato','cheese']
}

print("you ordered a "+ pizza['crust'] + " crust Pizza " +
    "\nwith the toppings:")

for topping in pizza['toppings']:
    print("\t\t"+topping)
