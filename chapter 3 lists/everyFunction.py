
cities = ['chennai','singapore','new york','london']
print(cities)

print('length of my list is '+str(len(cities)))

print("list Append")
cities.append('florence')
print(cities)

print("list insert")
cities.insert(3,'amsterdam')
print(cities)

print("list delete item")
del(cities[0])
print(cities)

print("list pop item")
pop_city = cities.pop(0)
print(cities)
print("popped city is "+pop_city)

print("list remove item (london)")
cities.remove('london')
print(cities)

print("list sort")
cities.sort()
print(cities)

print("list reversed")
cities.reverse()
print(cities)

print("reverse again")
cities.reverse()
print(cities)

print("sort without changing the list order")
print(sorted(cities))

