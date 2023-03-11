#Made into functions to show Claire
#Code still passes check50 so keeping it

import random


#Prompts the user for a level n,
#If the user does not input a positive integer, the program should prompt again.

not_level = 0

def get_level(x):
    while True:
        try:
            x = int(input("Level: "))
        except ValueError:
            continue
        if x <= 1:
            continue
        return x

#Randomly generates an integer between 1 and n inclusive, using the random module.


def play_game():
    while True:
        #Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        #If the guess is the same as that integer, the program should output Just right! and exit.
        if guess == target:
            print("Just right!")
            break
        #If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        elif guess < target:
            print("Too small!")
            continue
        #If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        elif guess > target:
            print("Too large!")
            continue
        break



level = get_level(not_level)

print(level)
target = random.randint(1, level)

play_game()

