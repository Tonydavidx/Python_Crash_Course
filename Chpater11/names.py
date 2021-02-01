from name_function import get_formatter_name

print("Enter 'q' to quit program")
while True:
    first = input("\nGive me a first name: ")
    if first == 'q':
        break
    last = input("Give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}")