#Create an empty dictionary called list
list = {}

#Start a loop to be broken when the error specified is encountered
while True:
    #Specify code to catch exception on
    try:
        #Request an input and convert to lower case and strip whitespace from either side
        item = input("").lower().strip()
    #If specified error is encountered
    except EOFError:
        #Print empty line to move down one before printing
        print()
        #Break out of loop after specified error is encountered
        break

    #Set the entered key with the default value of 0 if not found
    #Will add +1 to the value
    list[item] = list.get(item, 0) +1

#for each 'keys' found in the sorted dictionary's keys
for keys in sorted(list.keys()):
    #Print the key's value, and then print the key in uppercase
    print(f"{list[keys]} {keys.upper()}")
