import json

filename = 'favorite_num.json'
number = input("what is your favorite Number ")

with open(filename, 'w') as f:
    json.dump(number, f)