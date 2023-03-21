import re
import sys

def main():
    print(parse(input("HTML: ")))

#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
    match = re.search(r"(?:https?\://)(?:www\.)?(?:youtube.com/embed/)(\w{11})(\")", s)
    if match:
        video = match.group(1)
        return f"https://youtu.be/{video}"
    else:
        return None


if __name__ == "__main__":
    main()
