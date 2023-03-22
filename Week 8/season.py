from datetime import date, datetime, timedelta
import sys
import inflect
num = inflect.engine().number_to_words

def main():
    date_str = input("Please enter a date (YYYY-MM-DD): ")
    minutes = time(date_str)
    song = convert(minutes)
    print(f"{song.capitalize()} minutes")

def time(m):
    try:
        inp_date = datetime.strptime(m, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid Date Format")
    cur_date = date.today()
    delta = cur_date - inp_date
    minutes = int(delta.days * 24 * 60)

    return minutes

def convert(s):
    song = str(num(s)).replace("and ", "")
    return song

if __name__ == "__main__":
    main()
