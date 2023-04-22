# Kristine Joy Barrina # BSCPE 1-5 # April 22, 2023
# Creating a program that reads a file then extract the even and odd numbers then place it in a two different text files.

# PSEUDOCODE

import tkinter as tk
from tkinter import *

# Open a file called numbers.txt
with open ("numbers.txt", "r") as numbers:
   
# Create a variable that contains all the numbers
    all_numbers = numbers.readlines()
    print (all_numbers)

# Use for loop with range of all numbers length
for i in range (len(all_numbers)):

# If number is even, put it in even.txt
    if (int(all_numbers [i]) % 2) == 0:
        # Append all even numbers in even.txt
        with open ("even.txt", "a") as even:
            even.write (all_numbers [i])
            i += 1
            print ("It's even!")

# If number is odd, put it in odd.txt
    else:
        # Append all odd numbers in odd.txt
        with open ("odd.txt", "a") as odd:
            odd.write (all_numbers [i])
            i += 1
            print ("It's odd!")
    
# Design output using tkinters
# Create an instance window
root = Tk ()

# Create the dimension of window
root.geometry ("450x150")
root.title ("Even and Odd Numbers")

# Create Label
label_window = Label (root, text = "Click here!", fg = "black", justify = CENTER, font = ("Arial", 14, "bold"))

# Create Buttons
button1 = Button (root, text = "EVEN")
button2 = Button (root, text = "ODD")
button3 = Button (root, text = "CLOSE")

#Let the pack method declares the position attributes
label_window.pack (fill = "both")
button1.pack ()
button2.pack ()
button3.pack ()

tk.mainloop()