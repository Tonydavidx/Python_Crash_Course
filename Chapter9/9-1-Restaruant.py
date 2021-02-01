class Restaurant:

    def __init__(self, r_name, r_type):
        """ define restaraunt name and type """
        self.name = r_name
        self.type = r_type

    def describe_restaurant(self):
        print(f"\nRestaruant name is {self.name} and type is {self.type}")

    def open_restaurant(self):
        print(f"the restaruant {self.name} is now open for Business")

restaurant1 = Restaurant('bates','motel')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

