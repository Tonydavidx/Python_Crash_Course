responses = {}

# a flag 
poll_active = True

while poll_active:
    # prompt for name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")

    # store the response in responses 
    responses[name] = response

    # find out if anyone else want to take the poll
    repeat = input("anybody else want to respond? (yes / no)")
    if repeat == 'no':
        poll_active = False

# polling is complete 
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")     
