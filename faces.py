#Function to replace
def replace(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

input = input("Tell me how you're feeling with an emoticon: ")

newsentence = replace(input)

print(newsentence)
