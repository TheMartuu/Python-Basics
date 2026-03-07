import pytest
from vote_counting import register_vote,load_candidates_list,save_candidate,show_winner,get_id,load_ids

def test_register_vote(tmp_path):
    """Checks if a vote for a candidate is registered"""
    test_file = tmp_path / 'candidates.json'
    candidates = [
        {"name": "Candidate 1", "votes": 0},
        {"name": "Candidate 2", "votes": 0}
    ]
    save_candidate(candidates, test_file)
    register_vote('Candidate 1', test_file)
    candidates_list = load_candidates_list(test_file)
    candidate = next(c for c in candidates_list if c["name"] == "Candidate 1")
    assert candidate["votes"] == 1

def test_get_id(tmp_path): 
    """Checks if a new ID is saved and registered"""
    test_file = tmp_path / 'people_ids_file.json'
    result = get_id('45784578',test_file)
    assert result == True 
    ids_list = load_ids(test_file)
    assert '45784578' in ids_list

def test_get_not_valid_id(tmp_path):
    """Checks if a new ID is not saved when its length has more that 8 digits """
    test_file = tmp_path / 'people_ids_file.json'
    result = get_id('457184578',test_file)
    assert result == False

def test_get_repeated_id(tmp_path):
    """Checks if a new ID is saved when its length is 8 digits"""
    test_file = tmp_path / 'people_ids_file.json'
    get_id('45784578',test_file)
    repeated = get_id('45784578',test_file)
    assert repeated == False

def test_register_vote_updates_count(tmp_path):
    """Checks if the total results are displayed"""
    test_file = tmp_path / 'candidates.json'
    candidates = [
        {"name": "Candidate 1", "votes": 0},
        {"name": "Candidate 2", "votes": 0}
    ]
    save_candidate(candidates, test_file)
    register_vote('Candidate 1', test_file)
    candidates_list = load_candidates_list(test_file)
    assert candidates_list == [{"name": "Candidate 1", "votes": 1},{"name": "Candidate 2", "votes": 0}]

def test_get_winner(tmp_path): 
    """Displays winner"""
    test_file = tmp_path / 'candidates.json'
    candidates = [
        {"name": "Candidate 1", "votes": 15},
        {"name": "Candidate 2", "votes": 20}
    ]
    save_candidate(candidates, test_file)
    candidates_list = load_candidates_list(test_file)
    winner = show_winner(test_file)
    assert winner == {"name": "Candidate 2", "votes": 20}
    


