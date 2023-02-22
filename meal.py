def main():
    time_str = input("Please input the time in 24-hour format: ")
    time = convert(time_str)

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print()


def convert(deftime):
    hours, minutes = deftime.split(":")
    mealtime = float(hours) + float(minutes) / 60
    return mealtime

if __name__ == "__main__":
    main()
