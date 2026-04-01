from random import randint
import sys

correct_number = randint(1,100)

print("Welcome to the Number Guessing game.")
# prompt_number = int(input("Please enter your number: "))
prompt_difficulty = input("First, please enter your difficulty level:\n1. Easy (10 chances)\n2. Medium(5 chances)\n3. Hard (3 chances)\n >")

def get_difficulty_level(chosen_level):
    """Prompts user to select a difficulty level"""
    
    difficulty_levels = {
        '1':"easy",
        '2':"medium",
        '3': "hard"
    }
    if chosen_level in difficulty_levels.keys():
        print(f"You chose {difficulty_levels[chosen_level].capitalize()}")
        return difficulty_levels.get(chosen_level)
    
def calculate_tries(chosen_difficulty):
    """Calculates max number of tries when the difficulty level is set"""
    max_tries_by_level ={
        'easy' : 10,
        'medium': 5,
        'hard': 3
    }
    return max_tries_by_level.get(chosen_difficulty)


while prompt_difficulty not in ['1','2','3']: 
    print("Not valid!")
    prompt_difficulty = str(input("Try again!: "))
else:
    difficulty = get_difficulty_level(prompt_difficulty)
    tries = calculate_tries(difficulty)
    print(f"Okay. You get {tries} tries")

while True:
    try:
        prompt_number = int(input("Select a number between 1 and 100: "))
        break
    except ValueError:
        print("Not valid! Please enter a number.")

attempts = 0
while tries >= 0:
    if prompt_number < correct_number:
        print("Too low! The correct number is higher.")
        tries -= 1
        attempts += 1
        prompt_number = int(input("Try again!: "))
    elif prompt_number > correct_number:
        print("Too high! The correct number is lower.")
        tries -= 1
        attempts += 1
        prompt_number = int(input("Try again!: "))
    elif prompt_number == correct_number: 
        print(f"You got the correct number: {correct_number}! It took you {attempts} attempts!. ")
        break
    if tries == 1:
        print(f"Sorry, you lose! The correct number was {correct_number}")
        break

    


