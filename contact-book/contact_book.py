import json 
from pathlib import Path

file = Path('contacts.json')

def load_contacts(): 
    """checks if there's an existing file or creates another one if not"""
    if file.exists():
        with open(file,"r",encoding="utf-8") as f: 
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_contact(contacts): 
    """converts data and saves contact in the json file"""
    with open(file,"w",encoding="utf-8") as f: 
        json.dump(contacts,f,ensure_ascii=False,indent=2)

def display_contacts(): 
    """Displays current contacts in json file"""
    contact_list = load_contacts()
    if not contact_list:
        print("Contact list is empty")
        return 
    for contact in contact_list:
        print (f"Name: {contact['name']} - Phone: {contact['phone']}")


def add_contact(name,phone): 
    """adds contact's name and phone to the json file"""
    """if a contact already exists, it will not be saved"""
    contact_list = load_contacts()

    name = name.title()

    if any(contact["name"]== name for contact in contact_list):
        print("The contact already exists!")
        return 
    
    else: 
        new_contact = {
        "name" : name,
        "phone" : phone
    }
        contact_list.append(new_contact)
        save_contact(contact_list)
        print("Contact saved!")
    

def update_contact(name,phone): 
    """updates an existing contact"""
    contact_list = load_contacts()
    for contact in contact_list: 
        if contact["name"] == name: 
            contact["phone"] = phone
            save_contact(contact_list)
            print("New contact data saved!")
            return
    print("Contact not found! ")

def delete_contact(name):
    """deletes an existing contact"""
    name = name.title()
    contact_list = load_contacts()
    for contact in contact_list: 
        if contact["name"] == name: 
            contact_list.remove(contact)
            save_contact(contact_list)
            print("Contact deleted!")
            return 
    print("Contact not found!")

if __name__ == "__main__":     
    active = True

    message = "Welcome to the contact book! "
    print(message)
    prompt_user_option = input("Please enter an option:\n 1: Show contacts\n 2: Add a new contact\n 3: Edit an existing contact: \n 4: Delete an existing contact \n 5. Exit\n")

    while active:
        options = [1,2,3,4,5]
        try: 
            if int(prompt_user_option) == 1: 
                display_contacts()
                prompt_user_option = input("Please enter an option:\n 1: Show contacts\n 2: Add a new contact\n 3: Edit an existing contact: \n 4: Delete an existing contact \n 5. Exit\n")

            elif int(prompt_user_option) == 2: 
                prompt_new_name = input("Insert a name for the new contact: ")
                prompt_new_number = input("Insert a new phone for the contact: ")
                add_contact(prompt_new_name,prompt_new_number)
                prompt_user_option = input("Please enter an option:\n 1: Show contacts\n 2: Add a new contact\n 3: Edit an existing contact: \n 4: Delete an existing contact \n 5. Exit\n")
            
            elif int(prompt_user_option) == 3: 
                prompt_edit_name = input("Select what contact do you wish to edit: ")
                prompt_edit_number = input("Add the new number: ")
                update_contact(prompt_edit_name,prompt_edit_number)
                prompt_user_option = input("Please enter an option:\n 1: Show contacts\n 2: Add a new contact\n 3: Edit an existing contact: \n 4: Delete an existing contact \n 5. Exit\n")
            
            elif int(prompt_user_option) == 4: 
                prompt_delete_name = input("Select the name for the contact to be deleted: ")
                delete_contact(prompt_delete_name)
            
            elif int(prompt_user_option) == 5:
                active = False
                print('Bye!') 
            else:
                print('Option not valid!')
        except ValueError:
            print('Option not valid!')
            prompt_user_option = input("Please enter a valid option:\n 1: Show contacts\n 2: Add a new contact\n 3: Edit an existing contact: \n 4: Delete an existing contact \n 5. Exit\n")