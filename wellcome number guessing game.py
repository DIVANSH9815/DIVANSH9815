import random

minimum_num = 1
highest_num = 100
answer = random.randint(minimum_num, highest_num)
guesses = 0
is_running = True

print("WELCOME TO THE NUMBER GUESSING GAME!")
print(f"Your answer is between {minimum_num} and {highest_num}.")

while is_running:
    guess = input("Enter as guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < minimum_num or guess > highest_num:
            print("That number is out of range")
            print(f"please selecta number is between {minimum_num} and {highest_num}.")
        elif guess < answer:
            print("To low! try agian")
        elif guess>answer:
            print("To high!try agian")
        else:
            print(f"the answer is {answer}")
            print(f"the gusseses is: {guesses}")
            is_running = False
            
    else:
        print("Invalid")
        print(f"please select the number is between {minimum_num} and {highest_num}.")
