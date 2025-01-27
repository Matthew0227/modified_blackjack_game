import random
#adding 2 variation of blackjack game for gamemode
#Atlantic City Blackjack:
#Vegas Strip Blackjack:
#I'll add a betting system, a given amount of cash when you've started
#After the player stops playing, It'll display the statistics of the overall gameplay
#the total amount of played, how many times you've played in each variation, total win and lose, money at the end


#this tells that the player and dealer is playing at the beginning of the game
player_in = True
dealer_in = True
chips = 0
win = 0

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

def game_intro():
    width = 60
    right_justified = width//12
    print("🎉 Welcome to Blackjack! 🎉".center(width))
    print("=" * width)
    print("Dealer: Hello player, are you ready to test your luck and skills?".center(width))
    print("Dealer: Before we begin, please choose a game mode:".center(width))
    print("\n" + " 1. 🃏 Classic Mode".ljust(width // 2).center(width))
    print(" 2. 💪 Survival Mode".ljust(width // 2).center(width))
    print(" 3. 🎲 Blind Mode".ljust(width // 2).center(width))
    print(" 4. 🤝 Two Players".ljust(width // 2).center(width))
    print("\n" + "Dealer: Enter the number of your choice to get started (1-4)".center(width))

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

game_intro()

while True:
    gamemode = input("Please enter your gamemode(1-4): ")
    if not gamemode.isdigit() or int(gamemode) not in range(1, 5):
        print("Invalid input. Please enter a number between 1 and 4.")
    else:
        break

# Classic Mode Gameplay Core
if gamemode == '1':
    print("\n🎲 Starting Classic Mode!")
    chips = 1000
    while True:
       
        player_hand = []
        dealer_hand = []
        player_in = True
        dealer_in = True

        print(f"You have {chips} chips.")
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > chips or bet <= 0:
                    print("Invalid bet amount. Please bet within your available chips.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        for _ in range(2):
            deal_card(dealer_hand)
            deal_card(player_hand)

        while player_in or dealer_in:
            print(f"Dealer shows: {reveal_dealer_hand()} and X")
            print(f"You have {player_hand} for a total of {total(player_hand)}")

            if player_in:
                stay_or_hit = input("1: Stay\n2: Hit\n")
                if stay_or_hit == '1':
                    player_in = False
                else:
                    deal_card(player_hand)

            if total(dealer_hand) > 16:
                dealer_in = False
            else:
                deal_card(dealer_hand)

            if total(player_hand) > 21:
                print(f"You bust! Dealer wins.")
                chips -= bet
                break
            elif total(dealer_hand) > 21:
                print(f"Dealer busts! You win!")
                chips += bet
                break

        if total(player_hand) <= 21 and total(dealer_hand) <= 21:
            if total(player_hand) > total(dealer_hand):
                print(f"You win!")
                chips += bet
            elif total(player_hand) < total(dealer_hand):
                print(f"Dealer wins!")
                chips -= bet
            else:
                print("It's a tie!")

        print(f"Current chips: {chips}")


        continue_game = input("Play another round? (y/n): ").lower()
        if chips == 0:
            print("it seems like you don't have enough chips to continue,")
            print("here's 200 chips, welcome!")
            chips = 200
        if continue_game != 'y':
            break

    print("\n🎉 Thanks for playing Classic Mode!")
