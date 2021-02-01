file_path = 'guest_book.txt'

active = True
print("you can quit the program by entertin 'q'")
guest_name = ''

while active:
    guest_name = input("what is your name: ")
    with open(file_path, 'a') as text_object:
        text_object.write(f"{guest_name.title()} \n")
    if guest_name == 'q':
        break
    else:
        continue    


