from pyfiglet import Figlet
from random import choice
import sys
figlet = Figlet()

font_list = figlet.getFonts()

rand_font = str(choice(font_list))
print(rand_font)
#Prompts the user for a str of text.
#Zero arguments if the user would like to output text in a random font.
if len(sys.argv) == 1:
    #Prompts the user for a str of text.
    string = input("Enter a string of text: ")
    figlet.setFont(font=rand_font)
    print(figlet.renderText(string))

#Two arguments if the user would like to output text in a specific font
elif len(sys.argv) == 3:

    #in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        string = input("Enter a string of text: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(string))
    else:
        sys.exit("Incorrect arguments")
else:
    #If the user provides two command-line arguments and the first is not -f or --font
    #or the second is not the name of a font, the program should exit via sys.exit with an error message.
    sys.exit("Incorrect arguments")
