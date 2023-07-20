"""""
import random
roll = random.randint(1,6)
print("The computer rolled a " + str(roll))
"""
import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))
if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))
    