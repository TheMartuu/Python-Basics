import pytest
from contact_book import add_contact, load_contacts, update_contact, delete_contact

def test_add_contact(tmp_path):
    """Checks if a new contact can be added"""
    test_file = tmp_path / "contacts.json"
    result = add_contact('Larry', '1111', filepath=test_file)
    assert result['name'] == 'Larry'
    assert result['phone'] == '1111'

def test_add_duplicate_contact(tmp_path):
    """Checks if an already existing contact cannot be added again"""
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)
    result = add_contact('Larry', '1111', filepath=test_file) 
    assert result is None

def test_viewing_contact(tmp_path):
    """Checks if a contact already exists"""
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)
    contact_list = load_contacts(test_file)
    assert any(contact["name"] == "Larry" for contact in contact_list)

def test_edit_contact(tmp_path):
    """Checks if a contact can be edited if exists"""
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)
    update_contact('Larry','2222',filepath=test_file)
    contact_list = load_contacts(test_file)
    updated = next(c for c in contact_list if c["name"] == "Larry")
    assert updated['phone'] == '2222'

def test_edit_not_existing_contact(tmp_path):
    """Checks if a contact cannot be edited if doesn't exist"""
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)
    update_contact('Jack','3333',filepath=test_file)
    contact_list = load_contacts(test_file)
    updated = next(c for c in contact_list if c["name"] != "Jack")
    assert updated['phone'] == '1111'

def test_delete_contact(tmp_path):
    """Checks if an existing contact can be deleted"""
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)
    delete_contact ('Larry', filepath=test_file)
    contact_list = load_contacts(test_file)
    assert not any(contact["name"] == "Larry" for contact in contact_list)

def test_delete_not_existing_contact(tmp_path):
    """Checks that a not existing contact cannot be deleted""" 
    test_file = tmp_path / "contacts.json"
    add_contact('Larry', '1111', filepath=test_file)  
    contact_list = load_contacts(test_file)
    assert not any(contact["name"] == "Jack" for contact in contact_list)