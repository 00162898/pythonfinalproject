import urllib.request, urllib.parse, urllib.error
from random import randint
import random
import math


#Welcome screen
def title():
  print('<Welcome To The Quiz Game!>')
  input("\nPress Enter to continue...\n")

#all users must create an account and validate before starting the quiz
def greet():
  prompt_user = print('You must create a user account first.')
  firstname = input("Please enter your first name: ")
  firstname = firstname.lower()
  lastname = input("Please enter your last name: ")
  lastname = lastname.lower()

  # take the initial of the firstname and the whole lastname
  uname = firstname[0] + lastname[:]

  # output the username
  print("Your username is:", uname)
  # prompt for to create password
  pwd = input("Please create your password:"  )
  # save credentials to text file
  file = open("users.txt","a")
  file.write(uname)
  file.write(" ")
  file.write(pwd)
  file.write("\n")
  print ("Your credentials have been saved. \n")
  login() #call the login function to sign in

#function is called after creating a new user account to login and validate account
def login():
    uname = input("Now type your new username:"  )
    pwd = input("And type your new password:"  )
    #file = open("users.txt", 'w')
    file = open("users.txt","a")
    for line in open("users.txt","r").readlines(): # Read the lines
      credentials = line.split() # Split on the space, and store the results in a list of two strings
    if uname == credentials[0] and pwd == credentials[1]:
       print("Welcome new student!", uname,'\n')

    else:
      print("Bad Pass.")
      login() #returns to the top when wrong credentials


# display title for the quiz menu
def intro_menu():
    print("** The Quiz Game **\n")

# function display/print the menu options from a list for the quiz
# list add more options to the list later
def main_menu():
    main_options = ["1. Addition", "2. Trivia"]
    print(main_options[0])
    print(main_options[1])
    print('___________________________')


#functions is called to prompt user for the main menu option and validate for the the incorrect input options
def main_menu_input():
    main_input = int(input("Select from choices above: "))
    while main_input > 2 or main_input <= 0:
        print("Invalid menu option.")
        main_input = int(input("Please try again: "))
    else:
        return main_input

#function is called to print/display the math problem with equal sign and prompt user for the answer
def input_user_answer(math_problem):
    print("What's the answer?")
    print(math_problem, end="")
    result = int(input(" = "))
    return result

# verifies the user's input and counts for the correct answer
# list and tuples are randomly added to each response
def verify_answer(user_solution, math_answer, count):
    right = ("Good Job!", "Way to to!", "Awesome!")
    wrong = ["Wrong Sorry!", "No try it again!", "Not quite!"]
    if user_solution == math_answer:
        count = count + 1
        print(random.choices(right))
        return count
    else:
        print(random.choices(wrong))
        return count

# functions defines the random integers for the math problem, list, tuples for random response to user's input
# trivia question is also defined
def menu_option(index, count):
    right = ["Good Job!", "Way to to!", "Awesome!"]
    wrong = ("Wrong Sorry!" , "No try it again!" , "Not quite!")

    intger1 = random.randrange(1, 9)
    intger2 = random.randrange(1, 9)
    if index is 1:
        math_problem = str(intger1) + " + " + str(intger2)
        math_answer = intger1 + intger2
        user_solution = input_user_answer(math_problem)
        count = verify_answer(user_solution, math_answer, count)
        return count
    elif index is 2:
        print("\nHow many stars does the United States flag has?\n")
        print("A) 50")
        print("B) 67")
        print("C) 3")
        answer1=(input("\nWhat is your answer? (Choose a letter): \n").lower().title())
        #reply to user wrong or wrong random responses
        if answer1 == "A":
          print(random.choices(right))

        else:
          print(random.choices(wrong))



def main():
    title()
    greet()
    intro_menu()
    main_menu()


    option = main_menu_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = main_menu_input()



main()
