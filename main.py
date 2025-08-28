

"""

snake,water and gun game:

snake=-1
water=0
gun=1

"""

import random
computer=random.choice([0,-1,1])
user=input("Its your turn.\nEnter s for snake,w for water and g for gun: ")

you={"s": -1,"w": 0,"g":1}
reversedict={-1:"s",0:"w",1:"g"}
user=you[user]
print(f"Computer chosed: {reversedict[computer]}\nYou choosed: {reversedict[user]}")
if(computer==user):
    print("It's a draw. <_>")
else:
    if(computer==1 and user==-1):
        print("You lose! :(")
    elif(computer==1 and user==0):
        print("You win! :)")
    elif(computer==-1 and user==1):
        print("You win! :)")
    elif(computer==-1 and user==0):
        print("You lose! :(")
    elif(computer==0 and user==-1):
        print("You win! :)")
    elif(computer==0 and user==1):
        print("You lose! :(")
    else:
        print("Something went wrong. ^_^")
    


