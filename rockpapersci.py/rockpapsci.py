import random

print('ROCK, PAPER SCISSOR')
while True:
    print('Pick a choice\n 1. Rock\n 2. Paper\n 3. Scissor')
    user_choice=int(input())
    comp_choice = random.randint(1,3)
    while ((user_choice < 1) or (user_choice > 3)):
        print('Wrong input!!! Enter valid choice')
#user area
    if user_choice==1:
        choice_name="Rock"
    elif user_choice==2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("User's choice is", choice_name)

    # computer area
    if comp_choice==1:
        comp_name="Rock"
    elif comp_choice==2:
        comp_name = "Paper"
    else:
        comp_name = "Scissor"
    print("Computer's choice is", comp_name)

    print(choice_name, "V/S", comp_name)
    if ((user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1)):
        print("PAPER WINS!!!")
        result = "Paper"
    elif ((user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1)):
        print("ROCK WINS!!!")
        result = "Rock"
    elif ((user_choice == 1 and comp_choice == 1) or (user_choice == 2 and comp_choice == 2) or (
            user_choice == 3 and comp_choice == 3)):
        print("DRAW!!!")
        result = "DRAW"
    else:
        print("SCISSOR WINS!!!")
        result = "SCISSOR"

    if result == choice_name:
        print("USER WINS!!!")

    if result == "DRAW":
        print("DRAW, TRY AGAIN!!!")

    if result == comp_name:
        print("COMPUTER WINS")

    print("DO YOU STILL WANT TO PLAY AGAIN? Y/N")
    ans = input()
    if ans == 'n' or ans == 'N':
        break

print("THANKS FOR PLAYING!!!")





