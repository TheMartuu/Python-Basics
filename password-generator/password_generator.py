import string
import secrets

characters = list(string.ascii_letters) + list(string.digits) 

user_length = input("Please enter how many characters do you want for your password: ")

try: 
    user_length = int(user_length)
    if user_length < 8: 
        print("Not enough characters, please enter at least 8: ")
        user_length = int(input("Try again:  "))
    elif user_length > 20: 
        print("Too many characters, try entering less than 20:  ")
        user_length = int(input("Try again:  "))
except: 
    NameError
    print("Not valid! Enter a numeric value, please!")
    user_length = int(input("Try again:  "))


def generate_password(password_length): 
    return f''"".join([secrets.choice(characters) for i in range (1,password_length + 1)])

print('Your new password: ' + generate_password(user_length))