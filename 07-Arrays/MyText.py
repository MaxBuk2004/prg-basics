def count_words(text):
    words = text.split()
    return len(words)

def words_by_length(text):
    words = text.split()
    words_sorted = sorted(words, key=len, reverse=True)
    return words_sorted

def words_alphabetically(text):
    words = text.split()
    words_sorted = sorted(words)
    return words_sorted