# from car import Car, ElectricCar

# my_bettle = Car('VolksWagen', 'bettle', '2018')
# print(my_bettle.get_descriptive_name())
# # my_bettle.increment_odometer(25)
# # my_bettle.read_odometer()

# my_tesla = ElectricCar('tesla', 'model 5', 2021)
# print(my_tesla.get_descriptive_name())

# import car

# my_bmw = car.Car('bmw','X7',1998)
# print(my_bmw.get_descriptive_name())

# my_tesla = car.ElectricCar('Tesla','Roadster','2016')
# print(my_tesla.get_descriptive_name())



# from car import Car
# from electric_car import ElectricCar

# my_bmw = Car('bmw','X7',1998)
# print(my_bmw.get_descriptive_name())

# my_tesla = ElectricCar('Tesla','Roadster','2016')
# print(my_tesla.get_descriptive_name())


from car import Car
from electric_car import ElectricCar as EC

my_bmw = Car('bmw','X7',1998)
print(my_bmw.get_descriptive_name())

my_tesla = EC('Tesla','Roadster','2016')
print(my_tesla.get_descriptive_name())