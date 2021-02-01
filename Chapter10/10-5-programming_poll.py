file_path = 'programming_poll.txt'

print("you can quit the program by entertin 'q'")
name = ''

while True:
    name = input("\nwhat is your name: ")
    reason = input("why you like Programming: ")
    with open(file_path, 'a') as text_object:
        text_object.write(f"{name.title()} : {reason}\n")



            