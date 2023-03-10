month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date_str = input("Date: ")
    for char in date_str:

        if char == "/":
            month, day, year = date_str.strip().split("/")
            try:
                month = int(month)
                day = int(day)
                year = int(year)
            except ValueError:
                continue

            if not 1<= int(month) <= 12 or not 1<= day <= 31:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break

        elif char == ",":
            part1, year = date_str.strip().split(",")
            month_str, day = part1.split(" ")
            try:
                day = int(day)
                year = int(year)
            except ValueError:
                continue

            if month_str in month_names:
                if not 1<= int(month_names.index(month_str)+1) <= 12 or not 1<= day <= 31:
                    continue
                print(f"{year:02}-{month_names.index(month_str)+1:02}-{day:02}")
                break

            else:
                continue
    else:
        continue
    break
