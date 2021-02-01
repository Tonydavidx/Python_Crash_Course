file = 'C:/Users/Leonardo/Documents/python_crash_course/Chapter10/learning_python.txt'

# with open(file) as text_object:
#     contents1 = text_object.read()

# contents1 = contents1.replace('python','c#')
# print(contents1)

with open(file) as text_object:
    lines = text_object.readlines()

text = ''

for line in lines:
    text += line.strip()

print(text)

text2 = text.replace('python','java')

print(text2)