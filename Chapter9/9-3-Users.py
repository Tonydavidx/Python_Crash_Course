class User:

    def __init__(self, first_name, last_name, age, location):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("users name : "+ self.f_name + " " + self.l_name)
        print("users age : "+ str(self.age))
        print("users location: " +self.location)

    def greet_user(self):
        print(f"hello {self.f_name} {self.l_name} ")

    def user_location(self):
        print(f"{self.f_name} lives in {self.location}")    

user1 = User('leonardo','david',19,'avadi')

user1.describe_user()
user1.greet_user()
user1.user_location()