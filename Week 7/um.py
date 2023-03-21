import re

def main():
    print(count(input("Text: ")))


def count(s):
    if ums := re.findall(r"\bum\b", s, re.IGNORECASE):
        cnt = 0
        for _ in ums:
            cnt += 1
        return cnt
    else:
        return 0

if __name__ == "__main__":
    main()
