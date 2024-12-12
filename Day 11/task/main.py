from random import choices, choice
from typing import final

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_deck = (choices(card_deck, k=2))
player_deck = (choices(card_deck, k=2))

#Goes in a loop
def finalResult(player_deck, computer_deck, result):
    print(f"Your deck: {player_deck}")
    print(f"Dealers deck: {computer_deck}")
    print(f"You {result}!")


while True:
    if sum(player_deck) < 21 and sum(computer_deck) < 21:
        print(f"Your deck {player_deck}")
        print(f"Dealers first card {computer_deck[0]}")
        drawCard = (input("Type 'y' to get another card, type 'n' to pass:") == "y")
        if drawCard:
            player_deck.append(choice(card_deck))
            continue
        else:
            if sum(player_deck) < sum(computer_deck):
                finalResult(player_deck, computer_deck, "lose")
            else:
                finalResult(player_deck, computer_deck, "Win")
                break


    if sum(computer_deck) < 17:
            computer_deck.append(choice(card_deck))
    elif sum(player_deck) > 21 or sum(computer_deck) == 21:
        finalResult(player_deck, computer_deck, "Lose")
        break
    elif sum(player_deck) == 21 or sum(computer_deck) > 21:
        finalResult(player_deck, computer_deck, "Win")
        break
