

#0___>rock
#1___>papr
#2___>sisr
import random
game_on='y'
while game_on=='y':
    
        n=['0','1','2']

        
        computer=random.choice(n)

        user=int(input("enter your choice : "))


        if user==computer:
            print("DRAW!")

        elif (user==1 and computer==0):
            print("you won!")

        elif user==2 and computer==1:
            print("you won!")

        elif user==0 and computer==2:
            print("you won")

        else:
            print("computer won the match!")

        game_on=input("PLAY AGAIN? :(y/n) ")

        





