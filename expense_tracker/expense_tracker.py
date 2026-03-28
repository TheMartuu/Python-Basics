import json 
from pathlib import Path
from datetime import datetime

file = Path('expenses.json')

class Expense:
    def __init__(self,description,amount,category):
        """Create Expenses with attributes"""
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def convert_to_dict(self):
        """converts json file contents into a dictionary"""
        return {
            "description": self.description,
            "amount":self.amount,
            "category":self.category,
            "date":self.date
        }
    @classmethod
    def from_dict(cls, data):
        expense = cls(data["description"], data["amount"], data["category"])
        expense.date = data["date"]
        return expense
    
def load_expenses(filepath=file): 
    """Checks if file exists or creates a new one if not """
    if filepath.exists():
        with open(filepath, "r",encoding="utf-8") as f:
            try:
                data = json.load(f)
                return [Expense.from_dict(expense) for expense in data]
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses, filepath=file):
    """converts expenses to json and saves them into the file"""
    with open(filepath,"w",encoding="utf-8") as f: 
        json.dump([expense.convert_to_dict() for expense in expenses], f, ensure_ascii=False, indent=2)

def create_expense(description,amount,category,filepath=file):
    """creates expense and saves it into the Expenses object""" 
    expenses_list = load_expenses(filepath)
    #create Expense object with the data 
    new_expense = Expense(description,amount,category)
    expenses_list.append(new_expense)
    save_expenses(expenses_list,filepath)
    print("Saved!")
    return new_expense

def show_all_expenses(filepath=file): 
    """Displays all expenses"""
    expenses_list = load_expenses(filepath)
    if not expenses_list:
        print("Expense list is empty!")
        return 
    else: 
        for expense in expenses_list: 
            print(f"-Description: {expense.description}\n-Amount: {expense.amount}\n-Category: {expense.category}\n-Date: {expense.date}")


def expenses_by_category(filepath=file):
    """Filters expenses by category"""
    expenses_list = load_expenses(filepath)
    by_category = {}
    for expense in expenses_list:
        if expense.category in by_category: 
            by_category[expense.category] += expense.amount
        else: 
            by_category[expense.category] = expense.amount
    return by_category

if __name__ == "__main__":  
    active = True 
    print("Welcome to the expense tracker!")
    new_prompt = "What do you want to do?\n1. Register expense\n2.Show all expenses\n3.Filter by category\n4.Exit\nEnter option:"

    while active: 
        option = str(input(new_prompt))
        if option == "1": 
            prompt_description = str(input("Enter description for expense: "))
            prompt_amount = float(input("Enter amount: "))
            prompt_category = str(input("Add category: "))
            create_expense(prompt_description,prompt_amount,prompt_category)
        elif option == "2": 
            show_all_expenses()
        elif option == "3": 
            for category, total in expenses_by_category().items():
                print(f"{category}: ${total}")
        elif option == "4":
            print("Bye!")
            break
        else:
            print("Option not found! Try again...")
