import validators

address = input("Enter an email address: ")

print("valid") if validators.email(address) else print("Invalid")
