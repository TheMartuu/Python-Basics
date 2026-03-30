import pytest
from book_collection import Collection

def test_add_book_to_collection(tmp_path):
    """Checks if book is added to collection"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    new_book = collection.add_book_to_collection("Hamlet","Drama","1603","4")
    assert new_book.title == "Hamlet"
    assert new_book.genre == "Drama"
    assert new_book.year == "1603"
    assert new_book.rating == "4"

def test_display_book_collection(tmp_path):
    """Checks if a book collection has values"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    collection.add_book_to_collection("Hamlet","Drama","1603","4")
    collection.add_book_to_collection("Little Red Riding Hood","Fairytale","1023","3")
    assert collection.books[0].title == "Hamlet"
    assert collection.books[1].title == "Little Red Riding Hood"

def test_display_empty_collection(tmp_path):
    """Checks if an empty book collection has novalues"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    assert len(collection.books) == 0

def test_filter_book_by_category(tmp_path):
    """Checks if a book exists by category"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    collection.add_book_to_collection("Little Red Riding Hood","Fairytale","1023","3")
    result = collection.filter_by_genre("fairytale")
    assert len(result) == 1
    assert result[0].convert_to_dict() == {
        "title": "Little Red Riding Hood",
        "genre": "Fairytale",
        "year": "1023",
        "rating": "3"
    }

def test_non_existing_genre(tmp_path):
    """Checks if a non existing gender does not display any results"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    result = collection.filter_by_genre("action")
    assert result == None

def test_empty_genre(tmp_path):
    """Checks if an empty gender does not display any results"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    result = collection.filter_by_genre("")
    assert result == None

def test_filter_book_by_year(tmp_path):
    """Checks if a book exists by year"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    collection.add_book_to_collection("Little Red Riding Hood","Fairytale","1023","3")
    result = collection.filter_by_year("1023")
    assert len(result) == 1
    assert result[0].convert_to_dict() == {
        "title": "Little Red Riding Hood",
        "genre": "Fairytale",
        "year": "1023",
        "rating": "3"
    }

def test_non_existing_year(tmp_path):
    """Checks if a non existing year  does not display any results"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    result = collection.filter_by_year("2008")
    assert result == None

def test_empty_year(tmp_path):
    """Checks if an empty year does not display any results"""
    test_file = tmp_path / "book_collection.json"
    collection = Collection(test_file)
    result = collection.filter_by_year("")
    assert result == None