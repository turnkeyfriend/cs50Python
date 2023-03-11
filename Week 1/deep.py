def main():
    answer = str.lower(input("Please give the answer to the Ultimate Question: "))
    answer = str.strip(answer)
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
