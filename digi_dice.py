"""
Digi Dice
----------
Just a simply dice roller.
--------------------------
Disclaimer:
This is the first demo of this tool, there is no Error Handling in this version.
--------------------------
Coder: Ash Noor (ryn0f1sh)
Site: www.AshNoor.me

"""

# The imports
from time import sleep
from random import randint

# The Dice Rolling Function
def dice():
    print("\n[ ]-- Lets Roll --[ ]")
    sleep(1)

    # Variable: Ask the user for number range
    dice_size = input("Dice Size: ")

    # Variable: to hold the random number with in that range
    the_roll = randint(0, int(dice_size))

    # Display it on the screen.
    print("You Rolled: "+str(the_roll))

    # Call the another roll function.
    another_roll()


# The Again Function
def another_roll():
    print("\n// Another Roll //")

    # Ask if the user would like another roll
    ar_answer = input("Would you like to make an other roll?  Y/N: ")
    if ar_answer.lower() == 'y':
        # Call the Dice function
        dice()
    else:
        # Otherwise exit program
        print("Thanks for rolling. \nGoodbye")
        sleep(1)
        exit()




# Call the functions
if __name__ == "__main__":
    dice()