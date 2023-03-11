equation = input("Please enter a mathematical equation: ")

x, y, z = equation.split(" ")

x = float(x)
z = float(z)

match y:
    case "*":
        print(round(float(x * z), 1))
    case "/":
        print(round(float(x / z), 1))
    case "-":
        print(round(float(x - z), 1))
    case "+":
        print(round(float(x + z), 1))
