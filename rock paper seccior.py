import random
#0==rock:
#1==paper:
#2==scissor:
name=input("enter the name of the person who is ready to play:")
print("welcom to the rock paper scissor game",name)
print("enter the 0 for rock ,1 for papper,2 for scissor\n")
user_choice=int(input("enter the any one number from above\n"))
for i in range(0,3):
    computer=random.randint(0,2)
print(computer)
if user_choice<=2:
    if(user_choice==0) and (computer==3) or (user_choice==1) and (computer==0) or (user_choice==2) and (computer==1):
       print('YOU WIN THE GAME')
       print("congratulation",name)
    elif user_choice==computer:
        print("TIE UP THE GAME")
    else:
        print("YOU LOST THE GAME")
else:
    print("enter the above numbers which are given in the user_name")
