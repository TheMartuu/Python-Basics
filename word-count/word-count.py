from collections import Counter
from pathlib import Path

#Wuthering Heights text taken from https://gutenberg.org
file = Path('wuthering-heights.txt')

def load_text():
    """takes the text file and loads it as a string """
    content = file.read_text(encoding="utf-8")
    return content

def count_words(text): 
    """counts word quantity"""
    words = text.lower().split()
    return Counter(words)

def top_ten_words(counter): 
    for word, count in counter.most_common(10): 
        print(f"The word '{word}' is repeated {count} times.")

text_content = load_text()
counting_words = count_words(text_content)
top_ten_words(counting_words)