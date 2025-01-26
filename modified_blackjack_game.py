import random
#this tells that the player and dealer is playing at the beginning of the game
player_in = True
dealer_in = True

# deck of cards /  player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',]

player_hand = []
dealer_hand = []
# deal the cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 1
            else: 
                total += 11
    return total

# check for winner
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

# game loop

#deals the card 2 times to both dealer and player at the beginning of the game
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

while player_in or dealer_in:
    print(f"Dealer had {reveal_dealer_hand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if player_in:
        stay_or_hit = input("1: Stay\n2: Hit\n")
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if stay_or_hit == '1':
        player_in = False
    else:
        deal_card(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

#display for the result
if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Blackjack! You win!")
elif total(dealer_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Blackjack! You lose!")
elif total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You bust! Dealer wins!")
elif total(dealer_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer bust! You win!")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer wins!")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You win!")
elif total(dealer_hand) == total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("It's a tie!")