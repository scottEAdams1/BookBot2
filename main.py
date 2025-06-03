from stats import get_num_words, get_num_chars

#Reads out contents of book
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    print(f'{num_words} words found in the document')
    num_chars = get_num_chars(contents)
    print('Count of each char:')
    for char, count in num_chars.items():
        print(f"\t'{char}': {count}")


#Takes filepath for a book, returns contents of file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data


main()