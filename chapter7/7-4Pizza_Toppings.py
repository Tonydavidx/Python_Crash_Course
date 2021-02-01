print("please enter the toppings you want for your pizza: ")
print("enter enough to stop")
toppings = "What toppings you want: "
active = True

while active:
    topping = input(toppings)
    if topping == 'enough':
        active = False
    else:
        print("good choice i will add "+topping + " to your pizza")
