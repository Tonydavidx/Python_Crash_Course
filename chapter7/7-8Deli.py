sandwich_orders = ['cheese', 'pastrami','tuna', 'apple','pastrami','fish','pastrami','ham']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    print("sorry we ran out of pastrami")
    sandwich_orders.remove('pastrami')
    

while sandwich_orders: 
    order = sandwich_orders.pop()
    print(f"i am making you {order} sandwitch")
    finished_sandwiches.append(order)

print("\nthe sandwiches i made are: \n")

for fs in finished_sandwiches:
    print(fs)