import json 
from pathlib import Path 

file = Path('book_collection.json')

class Book: 
    """Creates an object to store a book's information"""
    def __init__(self,title,genre,year,rating):
        self.title = title
        self.genre = genre
        self.year = year 
        self.rating = rating

    def convert_to_dict(self):
        """converts json file contents into a dictionary"""
        return {
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": self.rating
        } 
    @classmethod
    def read_from_dict(cls, data):
        book = cls(data["title"], data["genre"], data["year"],data["rating"])
        return book


class Collection: 
    """Creates a Collection object"""
    def __init__(self, filepath=file):
        self.filepath = filepath
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.read_from_dict(book) for book in data]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []
    def save_collection(self,filepath=file):
        """Saves book collection"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([book.convert_to_dict() for book in self.books], f, ensure_ascii=False, indent=2)

    def add_book_to_collection(self,title,genre,year,rating):
        """Adds a book to a Collection"""
        new_book = Book(title,genre,year,rating)
        self.books.append(new_book)
        self.save_collection()
        print("Book added to collection!")
        return new_book
    

    def display_book_collection(self):
        """Displays collection"""
        if not self.books:
            print("Collection is empty!")
            return 
        for book in self.books:
            print(f"Title: {book.title}\nGenre: {book.genre}\nYear: {book.year}\nRating: {book.rating}\n-------------------------------")
    
    def filter_by_genre(self,filter_category): 
        """Filters books by genre"""
        results = []
        for book in self.books: 
            if book.genre.lower() == filter_category.lower(): 
                results.append(book)
        else: 
            print("Genre not found!")
            return 

    def filter_by_year(self,filter_year):
        """Filters books by year"""
        results = []
        for book in self.books: 
            if book.year.lower() == filter_year: 
                results.append(book)
        else: 
            print("Year not found!")
            return

if __name__== "__main__":
    collection = Collection()
    active = True 
    
    print("Welcome to the book collection!")
    while active: 
        prompt_option = str(input("What do you want to do?: \n1. View collection \n2. Add a Book \n3. Filter by genre \n4. Filter by year \n5. Exit \nSelected option:"))

        if prompt_option == "1": 
            collection.display_book_collection()
        elif prompt_option == "2": 
            prompt_title = input("Enter book title: ")
            prompt_genre = input("Enter genre: ")
            prompt_year = input("Enter year: ")
            prompt_rating = input("Enter rating: ")
            collection.add_book_to_collection(prompt_title,prompt_genre,prompt_year,prompt_rating)
        elif prompt_option == "3": 
            prompt_genre = input("Enter genre: ")
            collection.filter_by_genre(prompt_genre)
        elif prompt_option == "4": 
            prompt_year = input("Enter year: ")
            collection.filter_by_year(prompt_year)
        elif prompt_option == "5":
            print("Bye!")
            active = False
        else: 
            print("Option not found! Please try again")