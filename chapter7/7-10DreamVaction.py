vactions = {}
poll_on = True

while poll_on:
    names = input("what is your name ")
    vaction = input("if you could go anywhere in the world where would you go ")

    vactions[names] = vaction

    repeat = input("any one else want to take the poll (yes / no)")
    if repeat == 'no':
        poll_on = False

print("--- Poll Results ---\n")
for name,vaction in vactions.items():
    print(f"{name}  Would like to go to {vaction}")


print(vactions)
