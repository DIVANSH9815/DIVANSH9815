import random

# Slot machine symbols
symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']

# Function to spin the slot machine
def spin_slots():
    return [random.choice(symbols) for _ in range(3)]

# Function to check winnings
def check_winnings(spin, bet):
    if spin[0] == spin[1] == spin[2]:
        return bet * 10  # Jackpot
    elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin[2]:
        return bet * 3  # Small win
    return 0  # No win

# Main game loop
def play_slot_machine():
    balance = 100  # Starting balance
    while balance > 0:
        print(f"\nYour balance: ${balance}")
        bet = int(input("Enter your bet amount (or 0 to exit): "))
        if bet == 0:
            print("Thanks for playing! Goodbye!")
            break
        if bet > balance:
            print("You don't have enough balance to place this bet.")
            continue
        
        balance -= bet
        spin_result = spin_slots()
        print(f"Slot Machine: {' | '.join(spin_result)}")
        winnings = check_winnings(spin_result, bet)
        balance += winnings
        
        if winnings > 0:
            print(f"You won ${winnings}!")
        else:
            print("No win this time. Try again!")

    print("Game over! Your final balance is $", balance)

# Run the game
if __name__ == "__main__":
    play_slot_machine()python sloat 
