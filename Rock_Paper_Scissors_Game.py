# Rock Paper Scissors #4

import random# Computer Choice
def game():
    scores = [] #Empty List
    while True:#
        print("\n-----Welcome To Game-----")
        computer = random.choice([1,2,3]) # To Get Random Choices From Computer

        # User Choice
        user = input("R:Rock\nP:Paper\nS:Scissors\nChoose one :")

        # Dict
        youdict = {  "R" : 1 , "P" : 2 , "S" : 3 }
        reversdict = { 1 : "Rock" , 2 : "Paper" , 3 : "Scissor" }

        you =youdict[user.upper()]

        # We Get 2 Choices 
        print(f"\n-----Choices-----\nYour Choice : {reversdict[you]} \nComputer Choice : {reversdict[computer]}\n\n-----Result-----")

        # Game Logic

        # Draw
        if( computer == you ) :
            result = "IT'S DRAW"
            print(result)

        else :#Win or Lose
            if(computer == 1 and you == 3) or (computer == 2 and you == 1) or (computer == 3 and you == 2) :#Were You Lose
                result = "YOU LOSE !!"
                print(result)
           
            elif(computer == 3 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 3) :#were You Win
                result = "YOU WIN  !!!"
                print(result)

            else :#Problem 
                print("\n************* SOMETHING WENT WRONG *************")

        scores.append(result)

        dis = input("\nDisplay Score and Exit:").lower()

        if dis == "yes":
            print("\n-----Score List-----")
            for score in scores:
                print(score)
            break

        else:
            pass


game()