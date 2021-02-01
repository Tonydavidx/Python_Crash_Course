print("give me a number i will tell you if its multiple of ten or not")
number = input()
number = int(number)

if number % 10 == 0:
    print("the number "+str(number)+" is a multiple of Ten")
else:
    print("Number "+str(number)+" is not a multiple of ten")    