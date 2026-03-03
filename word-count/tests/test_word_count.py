import pytest
from collections import Counter
from word_count import count_words,top_ten_words

def test_correct_quantity_of_words():
    """Checks if the Counter class returns the correct number of elements"""
    counter = Counter({"hello": 5, "world": 3})
    result = top_ten_words(counter)
    assert result[0] == ("hello", 5)
    assert len(result) <= 2

def test_count_words_empty(): 
    """Checks if an empty Counter does not crash"""
    text = ""
    result = count_words(text)
    assert result == {}

def test_ten_elements(): 
    """Checks if the Counter class returns ten elements, even when the Counter has more"""
    counter = Counter({"word1": 1, "word2": 2, "word3": 3, "word4": 4, 
                       "word5": 5, "word6": 6, "word7": 7, "word8": 8, 
                       "word9": 9, "word10": 10, "word11": 11, "word12": 12})
    result = top_ten_words(counter)
    assert len(result) == 10

def test_count_words_case_insensitive():
    """Checks if the lowercase words and uppercase words are not counted as different words"""
    text = "hello Hello HELLO"
    result = count_words(text)
    assert result['hello'] == 3