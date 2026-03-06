import json 
from pathlib import Path 

candidates_file = Path('candidates.json')
people_ids_file = Path('people_ids_file.json')

def load_ids(filepath=people_ids_file):
    """loads file with people's ids if exists or creates another one if not"""
    if filepath.exists():
        with open(filepath,'r',encoding="utf-8") as f: 
            try: 
                return set(json.load(f))
            except json.JSONDecodeError:
                return set()
    return set()

def save_new_id(new_id,filepath =people_ids_file): 
    """saves new ID"""
    with open (filepath,'w',encoding="utf-8") as f: 
        json.dump(list(new_id),f,ensure_ascii=False,indent=2)

def load_candidates_list(filepath=candidates_file): 
    """loads file with candidates if exists or creates another one if not"""
    if filepath.exists():
        with open(filepath,'r',encoding="utf-8") as f: 
            try: 
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_candidate(candidates_list,filepath=candidates_file): 
    """saves new vote"""
    with open (filepath,'w',encoding="utf-8") as f: 
        json.dump(candidates_list,f,ensure_ascii=False,indent=2)

def get_id(new_voter_id,filepath=people_ids_file):
    """Validates IDs before voting"""
    voter_ids_list = load_ids(filepath)
    if len(new_voter_id) ==  8: 
        if new_voter_id not in voter_ids_list: 
            voter_ids_list.add(new_voter_id)
            save_new_id(voter_ids_list,filepath)
            return True
        else: 
            print("That ID is already registered, you cannot vote twice!")
            return False 
    else:
        print("ID not valid!")
        return False

def register_vote(candidate,filepath=candidates_file): 
    """Registers votes in the json file"""
    candidates_list = load_candidates_list(filepath)
    for register in candidates_list:
            if register['name'] == candidate:
                register['votes'] += 1
                save_candidate(candidates_list,filepath)
                print("Vote registered!")
                return 
    print("Candidate not found!")

def show_total_results(filepath=candidates_file):
    """Reads json file and displays total votes"""
    candidates_list = load_candidates_list(filepath)
    for candidate in candidates_list:
        print(f"{candidate['name']}: has {candidate['votes']} votes.")

def show_winner(filepath=candidates_file):
    """Displays the most voted candidate"""
    candidates_list = load_candidates_list(filepath)
    winner = (max(candidates_list, key=lambda c: c["votes"]))
    print(f"The winner is {winner['name']} with {winner['votes']} votes!")


                
if __name__ == '__main__':
    active = True
    menu_options = 'Welcome to the poll.'
    while active: 
        menu_options = str(input('Please enter options: \n1. Register vote \n2. Read results \n3. Check winner\n4. Exit \n'))
        if menu_options == '1':
            prompt_new_id = input("Please enter your ID: ")
            if get_id(prompt_new_id): 
                prompt_new_vote = input("Please enter your candidate: ")
                register_vote(prompt_new_vote)
        elif menu_options == '2':
            show_total_results()
        elif menu_options == '3':
            show_winner()
        elif menu_options == '4':
            print('Bye!')
            active = False
        else:
            print('Option not valid!')
    