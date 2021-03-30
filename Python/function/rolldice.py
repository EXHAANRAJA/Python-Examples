import random

def rolldice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def player():
    player1 = input("Enter Player 1 name:")
    player2 = input("Enter Player 2 name:")

    roll1 = rolldice()
    roll2 = rolldice() 

    print(player1 + " roll " + str(roll1))  
    print(player2 + " roll " + str(roll2))

    if  roll1 >  roll2:
        print(player1 + " win")
    elif roll2 >  roll1:
        print(player2 + " win")
    else:
        print("Tie")   

player()