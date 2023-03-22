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
    
    
 
# End
