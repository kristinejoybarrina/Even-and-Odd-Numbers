# Kristine Joy Barrina # BSCPE 1-5 # April 22, 2023
# Creating a program that reads a file then extract the even and odd numbers then place it in a two different text files.

# PSEUDOCODE

import tkinter as tk
from tkinter import *
import os

# Open a file called numbers.txt
with open ("numbers.txt", "r") as numbers:
   
# Create a variable that contains all the numbers
    all_numbers = numbers.readlines()

# Use for loop with range of all numbers length
for i in range (len(all_numbers)):

# If number is even, put it in even.txt
    if (int(all_numbers [i]) % 2) == 0:
        # Append all even numbers in even.txt
        with open ("even.txt", "a") as even:
            even.write (all_numbers [i])
            i += 1

# If number is odd, put it in odd.txt
    else:
        # Append all odd numbers in odd.txt
        with open ("odd.txt", "a") as odd:
            odd.write (all_numbers [i])
            i += 1
    
# Design output using tkinters
# Create an instance window
root = Tk ()

# Create the dimension of window
root.geometry ("450x150")
root.title ("Even and Odd Numbers")

# Create Label
label_window = Label (root, text = "Click here!", fg = "black", justify = CENTER, font = ("Arial", 14, "bold"))

# Define function 
def even_open ():
    os.startfile("even.txt")
    
def odd_open ():
    os.startfile("odd.txt")

# Create buttons with commands
even_button = Button (root, text = "EVEN", bg = "yellow", command = even_open)
odd_button = Button (root, text = "ODD", bg = "yellow", command = odd_open)
close_button = Button (root, text = "CLOSE", fg = "white", bg = "red", command = root.destroy)

#Let the pack method declares the position attributes
label_window.pack (fill = "both")
even_button.pack ()
odd_button.pack ()
close_button.pack (side = "bottom")

tk.mainloop()