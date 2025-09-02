import getpass

def get_bet(player, max_marbles):
    while True:
        try:
            bet_input = getpass.getpass(f"{player}, enter your bet (hidden input): ")
            bet = int(bet_input)
            if 1 <= bet <= max_marbles:
                return bet
            else:
                print(f"Please enter a number between 1 and {max_marbles}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_guess(player):
    while True:
        guess = input(f"\n{player}, guess if the number of marbles is odd or even (o/e): ").lower()
        if guess in ['o', 'e']:
            return guess
        else:
            print("Invalid input. Type 'o' for odd or 'e' for even.")

def main():
    player1_marbles = 10
    player2_marbles = 10

    print("\nWelcome to the Two-Player Marbles Game!\n")
    print("Each player starts with 10 marbles.")
    print("Try to win all your opponent’s marbles by guessing correctly!\n")

    current_player = "Player 1"
    other_player = "Player 2"

    while player1_marbles > 0 and player2_marbles > 0:
        print(f"\n{current_player} has {player1_marbles if current_player == 'Player 1' else player2_marbles} marbles.")
        print(f"{other_player} has {player2_marbles if other_player == 'Player 2' else player1_marbles} marbles.\n")

        max_bet = player1_marbles if current_player == "Player 1" else player2_marbles

        print(f"{current_player}, it's your turn to bet marbles (keep it secret!).")
        bet = get_bet(current_player, max_bet)

        guess = get_guess(other_player)

        actual = 'o' if bet % 2 == 1 else 'e'

        if guess == actual:
            print(f"{other_player} guessed correctly and wins {bet} marbles!")
            if other_player == "Player 1":
                player1_marbles += bet
                player2_marbles -= bet
            else:
                player2_marbles += bet
                player1_marbles -= bet
        else:
            print(f"{other_player} guessed wrong. {current_player} wins {bet} marbles!")
            if current_player == "Player 1":
                player1_marbles += bet
                player2_marbles -= bet
            else:
                player2_marbles += bet
                player1_marbles -= bet

        current_player, other_player = other_player, current_player

    if player1_marbles <= 0:
        print("\nPlayer 2 wins all the marbles! Game over.")
    else:
        print("\nPlayer 1 wins all the marbles! Game over.")

if __name__ == "__main__":
    main()
