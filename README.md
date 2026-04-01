🐍 Python Basics
A collection of small Python projects built to practice core programming concepts like functions, classes, dictionaries, lists, sets, and file persistence with JSON.

📁 Projects
📒 Contact Book
A CLI contact manager that stores contacts in a JSON file.
Concepts: dictionaries, functions, JSON persistence

Add, update, delete and display contacts
Duplicate contact detection using any()


📚 Book Collection
An inventory system for managing a personal book collection.
Concepts: classes, list comprehensions, OOP, JSON persistence

Book class with title, genre, year and personal rating
Collection class to manage the full inventory
Filter books by genre or year


💸 Expense Tracker
A personal finance tracker to log and categorize expenses.
Concepts: classes, classmethod, list comprehensions, JSON persistence

Expense class with to_dict and from_dict methods for JSON serialization
Group and sum expenses by category
Includes pytest test suite


✅ Task CLI
A command-line task manager to organize pending work.
Concepts: functions, dictionaries, JSON persistence, datetime

Add, update, delete and display tasks
Task status tracking (to do / in progress / done)
Includes pytest test suite


🗳️ Voting System
A simple poll system with duplicate vote prevention.
Concepts: sets, dictionaries, JSON persistence

Candidates stored in JSON with vote counts
Voter IDs tracked in a set to prevent double voting
ID format validation


📝 Word Counter
Analyzes a text file or URL and returns the most frequent words.
Concepts: dictionaries, collections.Counter, functions, requests

Fetches text directly from a URL using requests
Uses Counter.most_common() to find the top 10 words
Includes pytest test suite


🔢 Number Guess
A classic number guessing game.
Concepts: loops, conditionals, random

Random number generation
Feedback on each guess (too high / too low)


🔑 Password Generator
Generates secure random passwords based on user preferences.
Concepts: sets, functions, random, string

Choose to include letters, numbers and/or symbols
Configurable password length


🏷️ Barcode Generator
Generates barcodes from user input.
Concepts: external libraries, file output

✅ Luhn Algorithm
Implementation of the Luhn algorithm to validate credit card numbers.
Concepts: lists, mathematical logic, functions

🛠️ Tech Stack

Language: Python 3
Data persistence: JSON
Testing: pytest
External libraries: requests, collections


🚀 Getting Started
Clone the repository and navigate to any project folder:
bashgit clone https://github.com/TheMartuu/Python-Basics.git
cd Python-Basics/<project-folder>
python <main_file>.py
To run tests (where available):
bashpytest tests/

📌 About
These projects were built as a learning exercise to practice Python fundamentals. Each one focuses on one or more core concepts and grows progressively in complexity.
