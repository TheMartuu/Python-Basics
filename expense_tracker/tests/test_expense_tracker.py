import pytest
from expense_tracker import create_expense, load_expenses, expenses_by_category
from expense_tracker import Expense

def test_expense_creation(tmp_path): 
    """Tests if an expense is created"""
    test_file = tmp_path / 'expenses.json'
    new_expense = create_expense("Meat and Tomatoes",1500.0,"Food",filepath=test_file)
    assert new_expense.description == "Meat and Tomatoes"
    assert new_expense.amount == 1500.0
    assert new_expense.category == "Food"

def test_saved_expense(tmp_path):
    """Checks if a file is saved in the json file""" 
    test_file = tmp_path / 'expenses.json'
    create_expense("Meat and Tomatoes", 1500.0, "Food", filepath=test_file)
    expenses_list = load_expenses(test_file)
    assert expenses_list[0].description == "Meat and Tomatoes"

def test_empty_expenses (tmp_path):
    """Checks if and empty file returns and empty result""" 
    test_file = tmp_path / 'expenses.json'
    expenses_list = load_expenses(test_file)
    assert len(expenses_list) == 0

def test_expenses_by_category(tmp_path):
    """Checks that two expenses of the same category are saved""" 
    test_file = tmp_path / 'expenses.json'
    create_expense("Meat and Tomatoes",1500.0,"Food",filepath=test_file)
    create_expense("Potatoes",500.0,"Food",filepath=test_file)
    category_quantity = expenses_by_category(filepath=test_file) 
    assert category_quantity['Food'] == 2000.0

def test_expenses_by_category_multiple(tmp_path):
    """Checks that expenses of different category are not mixed""" 
    test_file = tmp_path / 'expenses.json'
    create_expense("Meat and Tomatoes",1500.0,"Food",filepath=test_file)
    create_expense("Potatoes",500.0,"Food",filepath=test_file)
    create_expense("Shirts",5000.0,"Clothes",filepath=test_file)
    create_expense("Pants",2500.0,"Clothes",filepath=test_file)
    categories = expenses_by_category(filepath=test_file)
    assert categories['Food'] == 2000.0
    assert categories['Clothes'] == 7500.0

def test_expense_to_dict():
    """Checks if an Expense is converted to a dictionary"""
    expense = Expense("Meat and Tomatoes", 1500.0, "Food")
    result = expense.convert_to_dict()
    assert result["description"] == "Meat and Tomatoes"
    assert result["amount"] == 1500.0
    assert result["category"] == "Food"
    assert "date" in result 

def test_dict_to_attribute():
    """Checks if an expense saved in a dictionary is converted into an object"""
    data = {"description": "Meat and Tomatoes", "amount": 1500.0, "category": "Food", "date": "2026-03-28 10:00:00"}
    expense = Expense.from_dict(data)
    assert expense.description == "Meat and Tomatoes"
    assert expense.amount == 1500.0 
    assert expense.category == "Food"
    