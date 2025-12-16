""" Task book
Vytvořte třídu Book, která reprezentuje knihu. Kniha bude mít atributy:
- title (název)
- author: Person?
- year
- pages
- isbn
- genre (žánr): str
- language (jazyk): str

+ dunder methods
+ properties (kde dává smysl)
"""
import datetime


class Book:

    def __init__(self, title: str, author: str, year: int, pages: int, isbn: str, genre: str,
                 language: str):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.isbn = isbn  # TODO rules for ISBN
        self.genre = genre
        self.language = language

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year})"

    def __str__(self):
        return f"Kniha: {self.title} od {self.author} ({self.year})"

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __len__(self):
        return self._pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        if not isinstance(title, str):
            raise TypeError("Title must be string.")
        if len(title) < 2:
            raise ValueError("Length of title must be more than 1.")
        self._title = title.strip().title()

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author: str):
        if not isinstance(author, str):
            raise TypeError("Author must be string.")
        self._author = author.strip().capitalize()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        if not isinstance(year, int):
            raise TypeError("Year must be integer.")
        if year > datetime.date.today().year:
            raise ValueError("Date can not be in future.")
        self._year = year

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Number of pages must be integer.")
        if pages <= 0:
            raise ValueError("Number of pages must be positive number.")
        self._pages = pages


if __name__ == "__main__":
    book1 = Book("Hlava XXII", "Joseph Heller", 2024, 528,
                 "484-46321-1231", "Román", "Čeština")
    print(f"book1: {book1}")

    book2 = Book("Egypťan Sinuhet", "  mika waltari", 2022, 832,
                 "789-589-13", "Historický román", "Čeština")
    print(f"book2: {book2}")

    book3 = Book(" hrabě monte cristo ", " alexandre dumas ", 2017, 736,
                 "7895-456-312", "Historický román", "Čeština")
    print(f"book3: {book3}")

    print("="*80)
    books = [book1, book2, book3]
    for book in books:
        print(f"{book} má {len(book)} stran.")

    print("=" * 80)
    if book1 > book2:
        print(f"{book1} je delší, než {book2}")
    else:
        print(f"{book2} je delší, než {book1}")

    print("=" * 80)
    book4 = Book("Hlava XXII", "Joseph Heller", 2024, 528,
                 "484-46321-1231", "Román", "Čeština")
    if book1 == book4:
        print(f"Knihu {book1} mám vícekrát.")
