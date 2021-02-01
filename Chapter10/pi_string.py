file_path = 'pi_digits.txt'
# file_path = 'thousands_of_pi.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))    


birthday = input("enter your birthday in the form (ddmmyy): ")
if birthday in pi_string:
    print("your birthday appears in the fake pi")
else:
    print("your birthday does not appear in the fake pi")    


