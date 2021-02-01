print("tell me something and i will repeat it back to you")
prompt = "\nEnter 'quit' to shut me up "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)