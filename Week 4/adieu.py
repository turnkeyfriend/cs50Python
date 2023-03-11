import inflect

p = inflect.engine()

names = []

#implement a program that prompts the user for names, one per line, until the user inputs control-d.
while True:
    try:
        name = input("")
    except EOFError:
        break

    names.append(name)

#separating two names with one and, three names with two commas and one and, and
#'n' names with 'n-1' commas and one 'and'
final = p.join(names)

print(f"Adieu, adieu, to {final}")
