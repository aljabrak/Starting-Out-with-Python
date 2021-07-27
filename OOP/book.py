# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 567.
# Algorithm Workbench.


class Book:

    def __init__(self, title, author_name, pages, pages_read):
        self.__book_title = title
        self.__author_name = author_name
        self.__book_pages = pages
        self.__pages_read = pages_read

    def set_title(self, title):
        self.__book_title = title
    
    def set_author(self, author_name):
        self.__author_name = author_name
    
    def set_pages(self, pages):
        self.__book_pages = pages

    def set_read_pages(self, pages_read):
        self.__pages_read = pages_read

    def __len__(self):
        return self.__book_pages

    def __repr__(self):
        return "\n" + str(self.__book_title) + "\n" + str(self.__author_name)

    def __str__(self, pages, pages_read):
        if pages_read/pages == 1:
            return "Completed " + str(self.__book_title)
        elif pages_read/pages >= 0.5:
            return "Read " + str(self.__pages_read) + " pages of " + str(self.__book_title) +"."
        elif pages_read/pages == 0.5:
            return "Read " + str(self.__pages_read) + " pages of " + str(self.__book_title) +"."
        elif pages_read/pages <= 0.5 and pages_read/pages > 0:
            return "Reading " + str(self.__book_title)
        else:
            return "Going to read this "+ str(self.__book_title) +"!"

def main():

    title = input("Book Name: ")
    author_name = input("Enter Author Name: ")
    pages = int(input("Enter Book Pages: "))
    pages_read = int(input("Enter Book Pages Read: "))

    book = Book(title, author_name, pages, pages_read)
    print(book.__repr__())
    print(book.__len__())
    print(book.__str__(pages, pages_read))

main()
