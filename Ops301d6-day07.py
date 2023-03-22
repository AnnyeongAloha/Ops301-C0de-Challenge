#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge
# Author: Justin 'Sage' Tabios
# Date of latest revision: 21 Mar 2023
# Purpose: Python script that generates all directories, subdirectories and files for a user-provided directory path.

#Main
import os 

# Variable for the path
path = input("Please enter a file path\n")

# Loop containing an array using the os.walk() function

for (root, dirs, files) in os.walk(path):
    print("Root:", root)
    print("Directories: ", dirs)
    print("Files: ", files)
    
    
# Saves output as a .txt file

# Script opens the .txt file with Libre Office Writer

# Add a Function to Python script that as a first step to prepare a test directory
# Takes a user input string
# Creates a directoryt named the string using os.makdirs function
# Create sub-directories within the directory names 'string_01','string_02','string_03'
# End
