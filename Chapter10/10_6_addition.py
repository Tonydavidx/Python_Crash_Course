print("a simple addition calculator")

first_number = input("First Number: ")
second_number = input("Second Number: ")

try:
    result = int(first_number) + int(second_number)
    print(result)
except ValueError:
    print("please enter integer only")
