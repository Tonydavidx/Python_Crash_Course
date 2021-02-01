import json

filename = 'favorite_num.json'
with open (filename) as f:
    num = json.load(f)

print(f"i know your favorite number it is {num}")    