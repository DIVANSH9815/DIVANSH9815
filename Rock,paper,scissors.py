import random


option = ("rock","paper","scissors")
player = None
print("-------------------------------------")
print("Wellcome to a ROCK PAPER SCISSORS GAME") 
print("Playing and injoying")          

while player is not option:
    computer = random.choice(option)
    running = True
    
    player = input("enter a player choice").lower()
    
    print(f"player: {player}")
    print(f"computer: {computer}")   
    
    if player == computer:
        print("TIE! Try agian")
    elif player == "rock"and computer == "paper":
        print("you win")   
    elif player == "paper"and computer == "pscissors":
        print("you win")   
    elif player == "scissors"and computer == "ppaper":
        print("you win")   
    else:
        print("you lose!try again")
        
    play_agian = input("enter a choice(y/n)").lower()
    if play_agian == "y":
        is_runnig = False
        print("thanks for playing")
