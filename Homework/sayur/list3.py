sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print("Unique Words in the Sentence:")
for word in unique_words:
    print(word)