# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("you cant divide by zero")    


print("give me two numbers and i will divide them.")
print("enter 'q' to Quit ")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
        
    except ZeroDivisionError:
        print("you cant divde a number by zero")

    else:
        print(answer)