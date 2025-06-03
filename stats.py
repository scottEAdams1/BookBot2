#Takes text as a string, returns number of words in string
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


#Takes text as string, returns number of instances for each character as a dictionary
def get_num_chars(text):
    dictionary = {}
    for char in text:
        char = char.lower()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary