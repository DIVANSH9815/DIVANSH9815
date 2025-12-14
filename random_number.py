import random

def game():
    print("----game is start----")
    score = random.randint(1, 50)

    with open("game.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"your score is:{score}")
    with open("game.txt","w") as f:
               f.write(str(score))
    return score    

game()
