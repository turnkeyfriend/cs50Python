import emoji


#prompts the user for a str in English
emoji_text = input("Please enter string: ")

#converting any codes (or aliases) therein to their corresponding emoji
emojified = emoji.emojize(emoji_text, language = "alias")

#outputs the “emojized” version
print(emojified)
