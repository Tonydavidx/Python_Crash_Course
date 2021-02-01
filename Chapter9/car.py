class Car:
    """ a simple attempt to represent a car """
    def __init__(self, maker, model, year):
        """ initialize attributes to descrive a car """
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ get neatly formatted decriptive name """
        long_name = f"{self.year} {self.maker} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """ update odometer to given value, also stop reject value that roll the odometer back """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can roll back an odometer")    

    def increment_odometer(self, miles):
        """ add a given amont to the odometer reading """
        self.odometer_reading += miles

    def read_odometer(self):
        """ print a statement showing cars milage change """
        print(f"this car has {self.odometer_reading} miles on it")    

# class Battery:
#     """ a simple attempt to model a battery for an elctric car """
#     def __init__(self, battery_size = 75):
#         self.battery_size = battery_size

#     def get_range(self):
#         """ print a statement about the range this battery provides """

#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"this car can go about {range} miles on a full charge")        

#     def describe_battery(self):
#         """ print the capcity of battery """
#         print(f"this car has a {self.battery_size}-Kw battery")

# class ElectricCar(Car):
#     """ represent aspects of a car, specific to electric vehicles """

#     def __init__(self, maker, model, year):
#         """ initializa attributes of the parent class """
#         super().__init__(maker, model, year)
#         # self.battery_size = 75
#         self.battery = Battery()

#     # def describe_battery(self):
#     #     """ describe the cars battery size """
#     #     print(f"this {self.maker} has a {self.battery_size}-KW Battery")

#     def available_gas(self):#this method over writes the parent class method
#         """ electric cars does not have gas tanks """
#         print("this is car does not have gas tank!")  

# used_car = Car('bmw','X6', 2011)
# print(used_car.get_descriptive_name())        

# new_car.odometer_reading = 26
# new_car.read_odometer()

# used_car.update_odometer(10)
# used_car.read_odometer()

# used_car.increment_odometer(50)
# used_car.read_odometer()

