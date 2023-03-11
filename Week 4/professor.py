#Adjust the printing out of total correct and answer when wrong
#Unhappy with having to making it less user friendly for the sake of passing the checks

#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
# digits. No need to support operations other than addition (+).
#Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
#the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
#If the user has still not answered correctly after three tries, the program should output the correct answer.
#The program should ultimately output the user’s score: the number of correct answers out of 10.
import random


def main():
    correct = 0
    level = get_level()

    for problems in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        for i in range(3):
            print(f"{x} + {y} = ?")
            try:
                guess = int(input("Answer: "))
            except ValueError:
                print("EEE")
                continue
            if guess == z:
                print("You're right!")
                print()
                correct += 1
                break
            if i == 2:
                print(f"THe answer was {z}.")
            else:
                print("EEE")

    print(f"You got {correct} out of 10 correct.")


def get_level():
    #Prompts the user for a level
    while True:
        try:
            x = int(input("Level: "))
            print()
        except ValueError:
            continue
        #If the user does not input 1, 2, or 3, the program should prompt again.
        if not 1<=x<=3:
            continue
        return x

#Return a randomly generated non-negative integer with -level- digits
def generate_integer(level):
    #10 to the power of (level - 1) Ex. For 3, 3-1 is 2, so 10 * 10 = 100
    min_num = 10**(level - 1)
    if level == 1:
        min_num = 0
    #(10 to the pwer of level) -1 Ex. For 3, 10 * 10 * 10 = 1000, minus 1 is 999
    max_num = (10**level)-1
    rand_num = random.randint(min_num, max_num)
    return rand_num


if __name__ == "__main__":
    main()
