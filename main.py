from stats import get_num_words

#Reads out contents of book
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    print(f'{num_words} words found in the document')


#Takes filepath for a book, returns contents of file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data


main()