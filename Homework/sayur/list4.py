sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split(' ')
unique_words = []
repeating_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
    elif word not in repeating_words:
        repeating_words.append(word)
print(unique_words)
print(repeating_words)

