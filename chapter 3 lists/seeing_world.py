locations = ['disney Land', 'singapore','ooty','scotland','japan']
print("my list original order")
print(locations)

print("my list sorted")
print(sorted(locations))

print("my list is still in original order")
print(locations)

print("my list in sorted reversed")
print(sorted(locations,reverse=True))

print("My list is still in original order")
print(locations)

locations.reverse()
print('List order is reversed')
print(locations)


print('List order is revered to the original list')
locations.reverse()
print(locations)

print("sorted list")
locations.sort()
print(locations)

print("sorting list and reversing")
locations.sort(reverse=True)
print(locations)