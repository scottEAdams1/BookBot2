#Reads out contents of book
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    num_words = number_of_words_in_string(contents)
    print(f'{num_words} words found in the document')


#Takes filepath for a book, returns contents of file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data


#Takes text as a string, returns number of words in string
def number_of_words_in_string(text):
    words = text.split()
    num_words = len(words)
    return num_words


main()