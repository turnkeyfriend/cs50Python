sentence = input("Please type a sentence: ")

words = sentence.split()

print(*words, sep = "...")
