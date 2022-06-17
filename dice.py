from random import randint

class Die():
    def __init__(self, name, sides=6,):
        self.sides = sides
        self.name = name

    def roll_die(self):
        print("\nRolling die...")
        print("You rolled a " + str(randint(1, self.sides)) + "!")

    def get_roll(self):
        return randint(1, self.sides)

die1 = Die('die1', 6)
die2 = Die('die2', 20)

def repeated_rolls(Die, num_rolls=1):
    for i in range(1, num_rolls + 1):
        Die.roll_die()

repeated_rolls(die1, 3)

        

