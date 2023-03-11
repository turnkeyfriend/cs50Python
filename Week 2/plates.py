def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(vanity):

#Check that length is between 2-6 characters
    if len(vanity) < 2 or len(vanity) > 6:
        return False

#Check that first 2 characters are not numbers
    if vanity[0].isalpha() == False or vanity[1].isalpha() == False:
        return False

#Check that the first number isn't a zero
    for i in range(len(vanity)):
        if vanity[i].isalpha() == False:
            if vanity[i] == "0":
                return False
            else:
                break
#Check that after a number is seen, characters after are not letters
    for i in range(len(vanity)):
        if vanity[i].isdigit():
            if not vanity[i:].isdigit():
                return False

#Check that there are no non-alphanumeric characters
    if vanity.isalnum() == False:
        return False

#If none of the test fail (are false) the return True to the main function
    return True



main()
