import random
#NEW: Statistics: win, lose, ties, chips, rounds
#NEW: 4 gamemodes: classic, survival, blinded, multiplayer (2players)


#this tells that the player and dealer is playing at the beginning of the game
player_in = True
dealer_in = True
chips = 0
rounds_played = 1
wins = 0
losses = 0
ties = 0
width_of_text = 60

player1_chips = 0
player2_chips = 0
player1_wins = 0
player2_wins = 0
player1_losses = 0
player2_losses = 0

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

def hidden_hand(turn):
    hidden_cards = []
    for cards in range(len(turn)):
        hidden_cards.append("X")
    return hidden_cards


game_intro()

while True:
    gamemode = input("Please enter your gamemode(1-4): ")
    if not gamemode.isdigit() or int(gamemode) not in range(1, 5):
        print("Invalid input. Please enter a number between 1 and 4.")
    else:
        break

if gamemode == '1':
    print("\n🎲 Starting Classic Mode!")
    chips = 1000
    while True:
       
        player_hand = []
        dealer_hand = []
        player_in = True
        dealer_in = True

        print(f"round {rounds_played}")
        print(f"You have {chips} chips.")
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > chips or bet <= 20:
                    print("Invalid bet amount. Please bet within your available chips.")
                elif bet <= 20:
                    print("Invalid bet amount. The minimum bet is 20.")
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
                print(f"You bust! Dealer wins")
                chips -= bet
                losses += 1
                rounds_played += 1
                break
            elif total(dealer_hand) > 21:
                print(f"Dealer busts! You win!")
                chips += bet
                wins += 1
                rounds_played += 1
                break

        if total(player_hand) <= 21 and total(dealer_hand) <= 21:
            if total(player_hand) > total(dealer_hand):
                print(f"You win!")
                chips += bet
                wins += 1
            elif total(player_hand) < total(dealer_hand):
                print(f"Dealer wins!")
                chips -= bet
                losses += 1
            else:
                print("It's a tie!")
                ties += 1
            rounds_played += 1

        print(f"Current chips: {chips}")

        while True:
            continue_game = input("Keep gambling? (y/n): ").lower()
            if continue_game == 'y':
                break
            elif continue_game == 'n': 
                break
            else:
                print("enter y/n: ")
        if chips == 0 or chips < 20:
            print("it seems like you don't have enough chips to continue,")
            print("here's 200 chips on the house, welcome!")
            chips += 200
        if continue_game != 'y':
                break
        
        

    print("\n🎉 Thanks for playing Classic Mode!".center(width_of_text))

if gamemode == '2':
    print("\n🎲 Starting Survival Mode!".center(width_of_text))
    print("Let's see how many wins you could do before your chips runs out".center(width_of_text))
    print("Winning won't earn your bets, you can only lose your chips".center(width_of_text))
    print("Goodluck playah".center(width_of_text))
    print("=" * width_of_text)

    chips = 1000
    while True:
       
        player_hand = []
        dealer_hand = []
        player_in = True
        dealer_in = True

        print(f"round {rounds_played}")
        print(f"You have {chips} chips.")
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > chips or bet <= 20:
                    print("Invalid bet amount. Please bet within your available chips.")
                elif bet <= 20:
                    print("Invalid bet amount. The minimum bet is 20.")
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
                print(f"You bust! Dealer wins")
                chips -= bet
                losses += 1
                rounds_played += 1
                break
            elif total(dealer_hand) > 21:
                print(f"Dealer busts! You win!")
                chips += bet
                wins += 1
                rounds_played += 1
                break

        if total(player_hand) <= 21 and total(dealer_hand) <= 21:
            if total(player_hand) > total(dealer_hand):
                print(f"You win!")
                wins += 1
            elif total(player_hand) < total(dealer_hand):
                print(f"Dealer wins!")
                chips -= bet
                losses += 1
            else:
                print("It's a tie!")
                ties += 1
            rounds_played += 1

        print(f"Current chips: {chips}")

        if chips == 0 or chips < 20:
            print("it seems like you've run out of chips")
            print("Tough luck, game over")
            break

        while True:
            continue_game = input("Keep gambling? (y/n): ").lower()
            if continue_game == 'y':
                break
            elif continue_game == 'n': 
                break
            else:
                print("enter y/n: ")

        if continue_game != 'y':
            break

    print("\n🎉 Thanks for playing Survival Mode!".center(width_of_text))

if gamemode == '3':
    print("\n🎲 Starting Blinded Mode!")
    chips = 1000
    while True:
       
        player_hand = []
        dealer_hand = []
        player_in = True
        dealer_in = True

        print(f"round {rounds_played}")
        print(f"You have {chips} chips.")
        while True:
            try:
                bet_player1 = int(input("Place your bet: "))
                if bet_player1 > chips or bet <= 20:
                    print("Invalid bet amount. Please bet within your available chips.")
                elif bet <= 20:
                    print("Invalid bet amount. The minimum bet is 20.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        for _ in range(2):
            deal_card(dealer_hand)
            deal_card(player_hand)

        while player_in or dealer_in:
            print(f"Dealer shows: {hidden_hand(dealer_hand)}")
            print(f"You have {hidden_hand(player_hand)} for a total of ?")

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
                print(f"You bust! Dealer wins")
                chips -= bet
                losses += 1
                rounds_played += 1
                break
            elif total(dealer_hand) > 21:
                print(f"Dealer busts! You win!")
                chips += bet
                wins += 1
                rounds_played += 1
                break

        if total(player_hand) <= 21 and total(dealer_hand) <= 21:
            if total(player_hand) > total(dealer_hand):
                print(f"You win!")
                chips += bet
                wins += 1
            elif total(player_hand) < total(dealer_hand):
                print(f"Dealer wins!")
                chips -= bet
                losses += 1
            else:
                print("It's a tie!")
                ties += 1
            rounds_played += 1

        print("Revealed cards".center(width_of_text))
        print(f"Dealer shows: {reveal_dealer_hand()} and X")
        print(f"You have {player_hand} for a total of {total(player_hand)}")
        print(f"Current chips: {chips}")

        while True:
            continue_game = input("Keep gambling? (y/n): ").lower()
            if continue_game == 'y':
                break
            elif continue_game == 'n': 
                break
            else:
                print("enter y/n: ")
        if chips == 0 or chips < 20:
            print("it seems like you don't have enough chips to continue,")
            print("here's 200 chips on the house, welcome!")
            chips += 200
        if continue_game != 'y':
                break
        
    print("\n🎉 Thanks for playing Blinded Mode!".center(width_of_text))

if gamemode == '4':
    print("\n🎲 Starting Multiplayer Mode!")
    player1_chips = 1000
    player2_chips = 1000
    while True:
       
        player_hand = []
        dealer_hand = []
        player_in = True
        dealer_in = True

        print(f"round {rounds_played}")
        print(f"Player 1 have {player1_chips} chips.")
        print(f"Player 2 have {player2_chips} chips.")
        while True:
            try:
                bet = int(input("Place the agreed upon bet: "))
                if bet > player1_chips and bet > player2_chips or bet <= 20:
                    print("Invalid bet amount. Please bet within your available chips.")
                elif bet <= 20:
                    print("Invalid bet amount. The minimum bet is 20.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        for _ in range(2):
            deal_card(dealer_hand)
            deal_card(player_hand)

        while player_in or dealer_in:
            

            if player_in:
                print("Player 1".center(width_of_text,"-"))
                print(f"You have {player_hand} for a total of {total(player_hand)}")
                stay_or_hit = input("1: Stay\n2: Hit\n")
                #to prevent the other player from seeing the opposite player's card
                for i in range(30):
                    print("")
                if stay_or_hit == '1':
                    player_in = False
                else:
                    deal_card(player_hand)

            if dealer_in:
                print("Player 2".center(width_of_text,"-"))
                print(f"You have {dealer_hand} for a total of {total(dealer_hand)}")
                stay_or_hit = input("1: Stay\n2: Hit\n")
                for i in range(30):
                    print("")
                if stay_or_hit == '1':
                    dealer_in = False
                else:
                    deal_card(dealer_hand)

            if total(player_hand) > 21:
                print(f"Player 1 bust! Player 2 wins")
                player1_chips -= bet
                player1_losses += 1
                player2_chips += bet
                player2_wins += 1
                rounds_played += 1
                break
            elif total(dealer_hand) > 21:
                print(f"Player 2 bust! Player 1 wins")
                player1_chips += bet
                player2_losses += 1
                player2_chips -= bet
                player1_wins += 1
                rounds_played += 1
                break

        if total(player_hand) <= 21 and total(dealer_hand) <= 21:
            if total(player_hand) > total(dealer_hand):
                print(f"Player 1 wins!")
                player1_chips += bet
                player2_losses += 1
                player2_chips -= bet
                player1_wins += 1
            elif total(player_hand) < total(dealer_hand):
                print(f"Player 2 wins!")
                player1_chips -= bet
                player1_losses += 1
                player2_chips += bet
                player2_wins += 1
            else:
                print("It's a tie!")
                ties += 1
            rounds_played += 1

        print(f"Player 1 chips: {player1_chips}")
        print(f"Player 2 chips: {player2_chips}")

        while True:
            continue_game = input("Keep playing? (y/n): ").lower()
            if continue_game == 'y':
                break
            elif continue_game == 'n': 
                break
            else:
                print("enter y/n: ")
        
        if continue_game != 'y':
                break
        
    print("\n🎉 Thanks for playing Multiplayer Mode!".center(width_of_text))

if gamemode == [1,2,3]:
    print("=" * width_of_text)
    print("📊 Game Statistics:".center(width_of_text))
    print(f"Total Rounds Played: {rounds_played}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Wins: {wins}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Losses: {losses}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Ties: {ties}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Final Chips: {chips}".ljust(width_of_text // 2).center(width_of_text))
    print("=" * width_of_text)
else:
    print("=" * width_of_text)
    print("📊 Game Statistics:".center(width_of_text))
    print(f"Total Rounds Played: {rounds_played}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Ties: {ties}".ljust(width_of_text // 2).center(width_of_text))
    print("=" * width_of_text)
    print(f"{'Player 1 Statistics:'}".center(width_of_text))
    print(f"Total Wins: {player1_wins}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Losses: {player1_losses}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Final Chips: {player1_chips}".ljust(width_of_text // 2).center(width_of_text))
    print("-" * width_of_text)
    print(f"{'Player 2 Statistics:':<20}".center(width_of_text))
    print(f"Total Wins: {player2_wins}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Total Losses: {player2_losses}".ljust(width_of_text // 2).center(width_of_text))
    print(f"Final Chips: {player2_chips}".ljust(width_of_text // 2).center(width_of_text))
    print("=" * width_of_text)