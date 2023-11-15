# We have all played snake, water gun game in our childhood.
#  If you haven't, google the rule of the game and write a python program
# capable of playing this game with the user.

import random

# Snake Water Gun or Rock Paper scisssors

def gameWin(comp,you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check For all possibilities when computer chosse s 
    elif comp == 's':
        if you == 'w':
            return False
        elif you=='g':
            return True
        
    # Check For all possibilities when computer chosse w
    elif comp =='w':
        if you =='g':
            return False
        elif you=='s':
            return True

    # Check for all possibilities when computer chose g 
    elif comp == 'g':
        if you=='s':
            return  False 
        elif you=='w':
            return True

print("Comp Turn: Snake(s) water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(W) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer Chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")