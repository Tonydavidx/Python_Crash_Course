print("a simple additopn calculator")

while True:
    first_number = input("First Number: ")
    try:
        n1 = int(first_number)
    except ValueError:
        print("please enter integer only")
    second_number = input("Second Number: ")
    try:
        n2 = int(second_number)
    except ValueError:
        print("please enter integer only")
        

    result = n1+n2
    print(result)        
