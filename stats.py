#Takes text as a string, returns number of words in string
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words