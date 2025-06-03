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

def sort_on(dict):
    return dict['num']

#Takes dictionary of character counts, returns ordered list of dictionaries for each character
def sort_num_chars(dictionary):
    unordered_list = []
    for item in dictionary.items():
        unordered_list.append({'char': item[0], 'num': item[1]})
    unordered_list.sort(reverse=True, key=sort_on)
    ordered_list = unordered_list
    return ordered_list