class Dog:#1
    """a simple attempt to model a dog"""#2
    # a function thats part of class is method
    # th init method runs automatically whenever we create new instance based on the class dog
    def __init__(self, name, age):#3
        """ Initialize name and age attributes """
        self.name = name#4
        self.age = age

    def sit(self):#5
        """ Simulate a dog sitting in response to a command """
        print(f"{self.name} is sitting")

    def roll_over(self):
        """ Simulate a roll over in respose to command """        
        print(f"{self.name} is rolling over")

my_dog = Dog('Jackie', 25)        
new_dog = Dog('wilson', 15)


print(f"My dogs name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dogs name is {new_dog.name}")
print(f"my dog is {new_dog.age} years old")
new_dog.sit()
new_dog.roll_over()
