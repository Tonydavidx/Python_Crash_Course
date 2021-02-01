file_path = 'guest.txt'

guest_name = input("whats is your name?: ")

with open (file_path, 'w') as file_object:
    file_object.write(guest_name)