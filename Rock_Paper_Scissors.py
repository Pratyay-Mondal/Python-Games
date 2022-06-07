import random

def Game(comp, you):
    if comp==you:
        return None

    elif comp=="Rock":
        if you=="p":
            return True
        elif you =="s":
            return False   

    elif comp=="Paper":
        if you=="r":
            return False
        elif you =="s":
            return True    

    elif comp=="Scissors":
        if you=="p":
            return False
        elif you =="r":
            return True    

print("Computer's Turn -> Rock / Paper / Scissors (computer has decided)")
n=random.randint(1,3)

if n==1:
    comp="Rock"
if n==2:
    comp="Paper"
if n==3:
    comp="Scissors"


you=input("Your Turn -> Rock(r) / Paper(p) / Scissors(s) : ")
if you=="r":
    your_choice="Rock"
elif you=="p":
    your_choice="Paper"
elif you=="s":
    your_choice="Scissors"

print("Computer's choice is : ", comp)
print("Your choice is : ", your_choice)

result=Game(comp, you)
if result==None:
    print("Ohh, It's a tie game")
elif result:
    print("Hurrah! You win the game")
else:
    print("Sorry! You lose the game")

