from stats import get_num_words, get_num_chars, sort_num_chars

#Reads out contents of book
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    num_chars = get_num_chars(contents)
    sorted_num_chars = sort_num_chars(num_chars)
    print_report(filepath, num_words, sorted_num_chars)
    


#Takes filepath for a book, returns contents of file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data

#Takes data, prints report in format
def print_report(filepath, num_words, sorted_num_chars):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char in sorted_num_chars:
        if char['char'].isalpha() == True:
            print(f'{char["char"]}: {char["num"]}')
    print('============= END ===============')


main()