# Program: Binary Teacher
# Author: Charlie Emmett
# Purpose: to help learn binary notation in a game format

import random

loop_flag = True

# print the instructions to the console

print("This game will help you practice translating integers to binary.")

print("The game will generate a random integer.")

print("You simply need to enter the binary equivalent of the provided number.")

print("Good luck.")

# begin loop

while loop_flag:

    # ask the user how many bytes they want to practice with

    byte_qty = int(input("How many bytes would you like to practice translating?"))

    print("Ok, we will practice with " + str(byte_qty) + " byte(s).")

    # calculate number of bits to print

    bits = 8 * byte_qty

    # generate random number

    rand_byte = random.randint(1, 255 * int(byte_qty))


    # format the random byte(s) to binary

    rand_binary = format(rand_byte, '08b')


    # give the user the byte(s) and collect their input

    user_binary = input("Convert " + str(rand_byte) + " to binary form.")

    if user_binary == rand_binary:

        print("Great job, you got it right.")

    else:

        print("Not quite, the correct answer was " + str(rand_binary))

    # Ask if the user wants to keep playing

    repeat = input("Do you want to try again? Please answer yes or no.")

    # if statement to break loop

    if repeat == "no":

        loop_flag = False
        
