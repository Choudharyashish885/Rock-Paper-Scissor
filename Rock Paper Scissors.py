import sys
from getpass import getpass
user1 = input("First player name: ")
user2 = input("Second player name: ")
user1_answer = getpass("%s,do you want to choose rock,paper,scissors?: " %user1)
user2_answer = getpass("%s,do you want to choose rock,paper,scissors?: " %user2)
def compare(user1_answer,user2_answer):
    if user1_answer==user2_answer:
        return("It's a tie!")
    elif user1_answer == "rock":
        if user2_answer == "scissors":
            return(user1,"Wins!")
        else:
            return(user2,"Wins!")
    elif user1_answer == "scissors":
        if user2_answer == "paper":
            return(user1, "Wins!")
        else:
            return(user2, "Wins!")
    elif user1_answer == "paper":
        if user2_answer == "rock":
            return(user1, "Wins!")
        else:
            return(user2, "Wins!")
    else:
        return("Invalid input! You have not enetered rock,paper,scissors,tryagain.")
        sys.exit()
print(compare(user1_answer,user2_answer))
