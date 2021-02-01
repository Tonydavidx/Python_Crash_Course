file = 'C:/Users/Leonardo/Documents/python_crash_course/Chapter10/learning_python.txt'

# with open(file) as text_object:
#     contents1 = text_object.read()

# print(contents1)


with open(file) as text_object:
    for contents2 in text_object:
        print(contents2.rstrip())


# with open(file) as text_object:
#     contents = text_object.readlines() 

# e_string = ''
# print(contents)

# for content in contents:
#     e_string += content.strip()

# print(e_string)