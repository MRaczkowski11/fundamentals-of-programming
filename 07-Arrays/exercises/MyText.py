# Liczba słów w tekście
def word_count(text):
    words = text.split()
    return len(words)


# Sortowanie słów od najdłuższego
def longest_words(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


# Sortowanie słów alfabetycznie
def alphabetical_words(text):
    words = text.split()
    return sorted(words)