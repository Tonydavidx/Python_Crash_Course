import json

filename = 'numbers.json'
with open(filename) as file:
    num = json.load(file)

print(num)    