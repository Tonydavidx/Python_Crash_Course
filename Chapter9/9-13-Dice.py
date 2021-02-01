from random import randint 

class Die:
    """ create a die and die rolling """
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        i = 0
        rolling = []
        while i < 10:
            i = i + 1
            rolling.append(randint(1,self.sides))

        print("results when rolling a 6 sides dice 10 times")
        for result in rolling:
            print(result)

    def roll_die_10(self):
        self.sides = 10
        i = 0
        rolling_10 = []
        while i < 10:
            i += 1
            rolling_10.append(randint(1,self.sides))

        print("\nresults when rolling 10 sided die 10 times: ")
        for result in rolling_10:
            print(result)

    def roll_die_20(self):
        self.sides = 20
        i = 0
        rolling_20 = []
        while i < 10:
            i += 1
            rolling_20.append(randint(1,self.sides))

        print("\nresults when rolling 20 sided die 10 times: ")
        for result in rolling_20:
            print(result)

        
die = Die()
die.roll_die()
die.roll_die_10()
die.roll_die_20()
