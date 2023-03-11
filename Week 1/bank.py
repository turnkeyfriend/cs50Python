greeting = str.lower(input("Please say hello however you would like: "))
greeting = str.strip(greeting)


if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
