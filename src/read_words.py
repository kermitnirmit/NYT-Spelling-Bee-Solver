def load_words():
    with open('../words/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
