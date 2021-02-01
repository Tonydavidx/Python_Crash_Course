available_toppings = ['chacolate','olives','mushrooms','cheese','pepper','anchives']
requested_toppings = ['chacolate','red pepper','olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding the topping "+ requested_topping
        )
    else:
        print("sorry, we dont have "+requested_topping)
            
print("\nFinished making your pizza")            