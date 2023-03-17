import csv
import sys

#Expects the user to provide two command-line arguments:
if not len(sys.argv) == 3:
    sys.exit("Please supply 2 arguments.")
elif not sys.argv[1].endswith(".csv") or not sys.argv[1].endswith(".csv"):
    sys.exit("Please ensure both arguments are .csv files.")

#Create empty list
db = []

#Open the file
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        #Go through each row, separate first/last names to variables
        for row in reader:
            last, first = row["name"].strip().split(", ")
            #Add first and last names from variables to list, and add house from the file
            db.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"The file {sys.argv[1]} does not exist.")

#Writing a new file with the newly created list
with open(sys.argv[2], "w", newline = "") as output:
    writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    #Using writerow (instead of rowS) causes it to use Keys() function, which won't work in a list with more than one dictionary
    #Would have needed a loop to use writerow instead of writerows
    writer.writerows(db)
    
#This will print out the newly created file contents in terminal
#with open(sys.argv[2], "r") as temp:
#    list = temp.read()
#    print(list)
