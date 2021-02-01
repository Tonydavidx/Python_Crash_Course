# def make_pizza(*toppings):
#     """ print toppings """
#     print(toppings)

# make_pizza('peporoni')
# make_pizza('almond','pepper','cheese')

# using for loop to print all toppings
# def make_pizza(*toppings):
#     """ print toppings """
#     print("\nMaking pizza with the following toppings")
#     for topping in toppings:
#         print(f"- {topping}") 

# make_pizza('peporoni')
# make_pizza('almond','pepper','cheese')


# this is module for another program to acces this function
def make_pizza(size,*toppings):
    """ summarize the pizza we are about to make """
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" -{topping}")

