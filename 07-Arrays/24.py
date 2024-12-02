import MyText

text = "An apple a day keeps the doctor away"

word_count = MyText.count_words(text)
words_by_length = MyText.words_by_length(text)
words_alphabetically = MyText.words_alphabetically(text)

print(f"Text: {text}")
print(f"Number of words: {word_count}")
print(f"Words from the longest: {', '.join(words_by_length)}")
print(f"Words ordered alphabetically: {', '.join(words_alphabetically)}")