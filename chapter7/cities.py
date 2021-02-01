prompt =("Enter the name of the cities you have visited: ")
prompt += "\nEnter quite when you are done"

while True:
    city =input(prompt)

    if city == 'quit':
        break
    else:
        print("i love to go to "+city.title())    