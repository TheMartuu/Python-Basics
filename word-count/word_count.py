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
    """returns the first most repeated words in the text"""
    return counter.most_common(10)
        

if __name__ == "__main__":
    text_content = load_text()
    counting_words = count_words(text_content)
    for word, count in top_ten_words(counting_words):
        print(f"The word '{word}' is repeated {count} times.")