class Restaurant:

    def __init__(self, r_name, r_type):
        """ define restaraunt name and type """
        self.name = r_name
        self.type = r_type
        self.number_served = 0    

    def describe_restaurant(self):
        print(f"\nRestaruant name is {self.name} and type is {self.type}")

    def open_restaurant(self):
        print(f"the restaruant {self.name} is now open for Business")

    def set_number_served(self, served_number):
        """ set the number of customers served """
        self.number_served = served_number

    def increment_number_served(self, increment):
        """ increase the number of customers served """
        self.number_served += increment

    def restaurant(self,):
        print(f"has served {self.number_served} customers")    

class IceCreamStand(Restaurant):
    """ copy retaruant class """
    def __init__(self, r_name, r_type):
        """  """
        super().__init__(r_name,r_type)
        self.flavoures = ['chcolate','vanilla','straberry']
        
    def describe_flavoures(self):
        print(f"offered flavoures are:")
        for f in self.flavoures:
            print(f)



# restaurant1 = Restaurant('bates','motel')
icecrem = IceCreamStand('macys','ice cream parlor')

# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()
# restaurant1.restaurant()

# restaurant1.set_number_served(50)
# restaurant1.restaurant()

# restaurant1.increment_number_served(100)
# restaurant1.restaurant()
icecrem.describe_restaurant()
icecrem.describe_flavoures()