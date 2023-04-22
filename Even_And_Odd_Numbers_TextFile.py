# Kristine Joy Barrina # BSCPE 1-5 # April 22, 2023
# Creating a program that reads a file then extract the even and odd numbers then place it in a two different text files.

# PSEUDOCODE

# Open a file called numbers.txt
with open ("numbers.txt", "r") as numbers:
   
# Create a variable that contains all the numbers
    all_numbers = numbers.readlines()
    print (all_numbers)

# Use for loop with range of 20
# If number is even, put it in even.txt
# If number is odd, put it in odd.txt
# Design output using tkinter