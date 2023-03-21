import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = "(1[0-2]|[0-9])(?::([0-5][0-9]))? ([AP]M)"
    if times := re.findall(rf"^{time} to {time}$", s):
        #print(times)
        hour1 = int(times[0][0])
        minute1 = times[0][1]
        ampm1 = times[0][2]
        hour2 = int(times[0][3])
        minute2 = times[0][4]
        ampm2 = times[0][5]
    else:
        raise ValueError

    if ampm1 == "PM" and hour1 != 12:
        hour1 += 12
    elif ampm1 == "AM" and hour1 == 12:
        hour1 = 0

    if ampm2 == "PM" and hour2 != 12:
        hour2 += 12
    elif ampm2 == "AM" and hour1 ==12:
        hour2 = 0
    if minute1 == "":
        return f"{hour1:02}:00 to {hour2:02}:00"
    else:
        return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"

if __name__ == "__main__":
    main()
