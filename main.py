#Reads out contents of book
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    print(contents)




#Takes filepath for a book, returns contents of file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data

main()