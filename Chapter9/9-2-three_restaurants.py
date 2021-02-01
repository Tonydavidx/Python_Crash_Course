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
restaurant2 = Restaurant('ichirakku','japanese')
restaurant3 = Restaurant('kokinava','shushi')


restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()
