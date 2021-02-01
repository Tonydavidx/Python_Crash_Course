import json 

try:
    filename = 'favorite.json'
    with open(filename) as f:
            number = json.load(f)
            print(f"your favorite number is {number}")
except FileNotFoundError:
    num = input("what is your favorite number: ")
    filename = 'favorite.json'
    with open (filename, 'w') as f:
        json.dump(num, f)
    print(f"your favorite number is {num} i will remember it ")
