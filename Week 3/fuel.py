#In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
#wherein each of X and Y is an integer, and then outputs,
#as a percentage rounded to the nearest integer, how much fuel is in the tank.
def main():
    while True:
        try:
            fraction = (input("Fraction: "))

            str_x, str_y = (fraction.split("/"))
            x = int(str_x)
            y = int(str_y)

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
            if x > y:
                print(end="")
                continue

            percent = int(round(x/y, 2)*100)
        except ValueError:
            print(end = "")
        except ZeroDivisionError:
            print(end = "")
        else:
            break

#If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")


main()
