#Dan Campbell
#4/12/2024
#P5HW
#Math Quiz Game

#import Random module
import random


#Define Functions
def main_menu():
    #Menu Layout
    print ("Welcome to Math Quiz")
    print()
    print()
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    #Ask user to select menu option
    choice = input("Please choose one of the Menu Options (1, 2, or 3): ")

    #Input Validation

    while choice.isdigit() == False:
        print ("Invalid Selection, you must enter a number (1, 2, or 3")
        choice = input("Please choose one of the Menu Options (1, 2, or 3): ")

    choice =int(choice)

    while not (choice == 1 or choice == 2  or choice ==3):
        print ("Invalid Selection")
        choice = int(input("Please choose one of the Menu Options (1, 2, or 3): "))

    #Launch Game
    if choice == 1:
        #Launch add_random_numbers
        add_random_numbers()

    elif choice == 2:
        #Launch Subtract_random_numbers
        subtract_random_numbers()

    elif choice == 3:
        print ("Thank You for playing...")
        print ("Bye!!!")
    
def add_random_numbers():
    #Define game variables
    guess_count = 0

    #Generate Random Numbers
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)

    #Calculate addition
    answer1 = num1 + num2

    #Display problem for user, prompt input for guess
    print (f'{num1:>4}')
    print (f'+{num2:>3}')
    guess = input("Enter a guess: ")

    #input validation
    while guess.isdigit() == False:
        print ("You must enter a number")
        guess = input ("Enter a new guess: ")
    guess = int(guess)

    #Calculate guess vs answer, inform user if high/low, iterate guess counter, prompt user for new input
    while guess != answer1:
        while guess > answer1:
            print ("Sorry, Your guess is to high")
            guess_count += 1 
            guess = input("Try Again: ")
            #input validation
            while guess.isdigit() == False:
                print ("You must enter a number")
                guess = input ("Enter a new guess: ")
            guess = int(guess)
        while guess < answer1:
            print ("Sorry, your guess is to low")
            guess_count += 1
            guess = input("Try Again: ")
            #input validation
            while guess.isdigit() == False:
                print ("You must enter a number")
                guess = input ("Enter a new guess: ")
            guess = int(guess)

    #iterate guess counter, display results when user is correct
    guess_count +=1
    print ("Congratulations!!! Your answer is correct.")
    print (f'Number of Guesses: {guess_count}')
    print ()
    print ()
    print ()

    #Prompt user to play again or return to menu
    print ("Please choose another option:")
    print ("1. Play Again")
    print ("2. Return to Menu")
    print ()
    con_choice = input ("Select 1 or 2: ")

    #input validation
    while con_choice.isdigit() == False:
        print ("Invalid Selection, you must enter a number (1 or 2")
        con_choice = input("Please choose one of the Menu Options (1 or 2: ")
    con_choice = int(con_choice)
    while not (con_choice == 1 or con_choice == 2):
        print ("Invalid Selection")
        con_choice = int(input("Please choose one of the Menu Options (1, 2, or 3): "))
    #execute menu options
    if con_choice == 1:
        #Launch add_random_numbers
        add_random_numbers()

    elif con_choice == 2:
        #Return to menu
        main_menu()    
    

def subtract_random_numbers():
    #Define game variables
    guess_count = 0

    #Generate Random Numbers
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)

    #Calculate addition
    answer1 = num1 - num2

    #Display problem for user, prompt input for guess
    print (f'{num1:>4}')
    print (f'-{num2:>3}')
    guess = int(input("Enter a guess: "))


    #Calculate guess vs answer, inform user if high/low, iterate guess counter, prompt user for new input
    while guess != answer1:
        while guess > answer1:
            print ("Sorry, Your guess is to high")
            guess_count += 1 
            guess = int(input("Try Again: "))
        while guess < answer1:
            print ("Sorry, your guess is to low")
            guess_count += 1
            guess = int(input("Try Again: "))
    #Due to the potential of negative numbers, I was unable to get input validation working for
    #this part of the program

    #iterate guess counter, display results when user is correct
    guess_count +=1
    print ("Congratulations!!! Your answer is correct.")
    print (f'Number of Guesses: {guess_count}')
    print ()
    print ()
    print ()

    #Prompt user to play again or return to menu
    print ("Please choose another option:")
    print ("1. Play Again")
    print ("2. Return to Menu")
    print ()
    con_choice = input ("Select 1 or 2: ")

    #input validation
    while con_choice.isdigit() == False:
        print ("Invalid Selection, you must enter a number (1 or 2")
        con_choice = input("Please choose one of the Menu Options (1 or 2: ")
    con_choice = int(con_choice)
    while not (con_choice == 1 or con_choice == 2):
        print ("Invalid Selection")
        con_choice = int(input("Please choose one of the Menu Options (1, 2, or 3): "))
    #execute menu options
    if con_choice == 1:
        #Launch add_random_numbers
        subtract_random_numbers()

    elif con_choice == 2:
        #Return to menu
        main_menu()    



#Launch Game
main_menu()






