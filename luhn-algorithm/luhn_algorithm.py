### The following code was inspired by the exercise given in CS50 course about Luhn's algorithm

def get_card_network(card): 
    """Gets card network taking the cards first digit"""
    card = str(card)
    networks = {
        '3' : 'American Express',
        '4' : 'Visa',
        '5' : 'Mastercard'
    }
    return networks.get(card[0],'OTHER')

def get_luhn(card): 
    """Calculates luhns algorithm in the given card number"""
    card = str(card)
    digits = list(map(int, card[::-1]))
    sum_of_digits = 0

    for i , j in enumerate(digits): 
        if i %2 == 1: 
            j *= 2
            if j > 9: 
                j -= 9
        sum_of_digits += j
    return (sum_of_digits %10 == 0)


valid_cards = [4242424242424242,4000056655665556,378282246310005,5555555555554444,6011111111111117]
not_valid_cards = [4242424242424243,5242424242424243,388282246310005]
print(get_luhn(valid_cards[2]))

def validate_cards (cards):
    """Prints if a card is valid with its respective network"""
    for card in cards: 
            luhn = get_luhn(card)
            if luhn: 
                print(f'Number: {card}\n{get_card_network(card).upper()}')
            else: 
                print(f'Not valid!')

validate_cards(valid_cards)
validate_cards(not_valid_cards)
