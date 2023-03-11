#implement a program that prompts the user for a str of text
#and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
#whether inputted in uppercase or lowercase.

def main():
    text = input("Enter text: ")
    final_text = no_vowel(text)
    print(f"{final_text}")

def no_vowel(temptext):
    for letter in temptext:
        if letter.lower() in ["a", "e", "i" ,"o" ,"u"]:
            temptext = temptext.replace(letter, "")
    return temptext

main()
