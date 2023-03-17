import csv
import sys
from tabulate import tabulate

#exit if not csv or not one argument
if not len(sys.argv) == 2:
    sys.exit("Please supply exactly 1 argument.")
#create empty list
menu = []

#Open csv file and read rows into the menu list
#Also catch if file does not exist and if file is not .csv
try:
    with open(sys.argv[1]) as file:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("File is not a .csv file")
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} does not exist.")

#print out using 'grid' format
print(tabulate(menu, headers = "firstrow", tablefmt = "grid"))

