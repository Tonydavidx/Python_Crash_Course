# motorcycles = ['Hero Honda','Ducati','Suzuki','Wolks Vogan']
# print(motorcycles)

# motorcycles[0] = 'Honda' 
# print(motorcycles)

# motorcycles.append('BMW')
# print(motorcycles)

motorcycles = []

motorcycles.append('Honda')
motorcycles.append('Volvo')
motorcycles.append('BMW')

# motorcycles.insert(1,'Audi')
# del motorcycles[0]
# popped_motorcycles = motorcycles.pop()
# last_car = motorcycles.pop(1)
expensive = 'Volvo'
motorcycles.remove(expensive)
print(motorcycles)
print("\nA " +expensive.title() +" is too expensive for me.")