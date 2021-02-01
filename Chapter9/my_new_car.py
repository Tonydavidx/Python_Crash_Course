from car import Car

my_new_car = Car('Audi','A85',2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 45
my_new_car.read_odometer()