import sys

if not len(sys.argv) == 2:
    sys.exit("Please provide one argument.")



lines = 0
try:
    with open(sys.argv[1]) as file:
        if not sys.argv[1][-3:] == ".py":
            sys.exit("Not a python file (.py)")
        for row in file:
            if row.lstrip().startswith("#") or row.strip() == "":
                pass
            else:
                lines += 1
except FileNotFoundError:
    print(f"{sys.argv[1]} does not exist.")

print(lines)
