# Rock paper Scissors
import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    
    if user_input == "exit":
        print("Game Ended! Goodbye!!")
        print("You won the total score of " + str(user_points) + " and the computer's total score is " + str(computer_points ))
        exit = True
        
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock!")
            print("The Computer's input is also rock!")
            print("It's a tie!!!")
        elif computer_input == "paper":
            print("Your input is rock!")
            print("The Computer's input is paper!")
            print("The computer wins..It's smarter than you!!!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock!")
            print("The Computer's input is scissors!")
            print("Finally you win!!!")
            user_points += 1            
    elif user_input == "paper":
         if computer_input == "rock":
            print("Your input is paper!")
            print("The Computer's input is rock!")
            print("You win..I'm Happy for you!!!")
            user_points += 1
    elif computer_input == "paper":
            print("Your input is paper!")
            print("The Computer's input is also paper!")
            print("It's a tie!!!")
    elif computer_input == "scissors":
            print("Your input is paper!")
            print("The Computer's input is scissors!")
            print("The computer wins..It's smarter than you!!!")
            computer_points += 1
            
            
    elif user_input == "scissors":
         if computer_input == "rock":
            print("Your input is scissors!")
            print("The Computer's input is rock!")
            print("The computer wins..It's smarter than you!!!")
            computer_points += 1 
    elif computer_input == "paper":
            print("Your input is scissors!")
            print("The Computer's input is paper!")
            print("Finally you win!!!")
            user_points += 1
    elif computer_input == "scissors":
            print("Your input is scissors!")
            print("The Computer's input is also scissors!")
            print("It's a tie!!!")
    
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" :
            print("Invalid Input! Try Again...")   
            






























