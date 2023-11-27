import random

cowbullcount=[]                                         #declared list
def compare_numbers(number, user_guess):
    current=0
    cows=0                                              #initializing variables
    bulls=0  
    for i in user_guess:
        if i in number:
            cows+=1
            if number[current]==i:
                bulls+=1
        current+=1                                      

    cowbullcount=[cows, bulls]                           
    return cowbullcount                                  #changed 'cowbull' to 'cowbullcount'

playing = True #gotta play the game
<<<<<<< HEAD
number = str(random.randint(1000,9999)) #random 4 digit number 
guesses = 0
# removed the 'print(number)' statement                                  
print(number)
=======
number = str(random.randint(0,9999)) #random 4 digit number 
guesses = 0
# removed the 'print(number)' statement                                  

>>>>>>> parent of 6f690fa (cow_bulls final version (fixed an error from v1.0 in line 9)))
print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")       #replaced 'raw_input' with input()
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was "+str(number)) #added guesses
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
