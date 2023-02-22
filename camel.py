#Create our main function
def main ():
    camel_case = input("Please input a name in camelcase: ")
    print("Here's the same but in snake case: ", end="")
    make_snake(camel_case)

#Create the function to convert to snake
def make_snake(name):
    for letter in name:
        if letter.isupper():
            print(f"_{letter.lower()}", end="")
        else:
            print(f"{letter}", end="")

main()
print()
