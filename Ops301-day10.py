# Ops302 Code Challenge Day-10 
# Author: Justin 'Sage' Tabios
# Date of revision: 24 Mar 2023
# Purpose: Create a script that opens a file, appends and prints the 3rd line and deletes the file. 

# Opens a new file named "myfile.txt" in write mode and appends 3 lines
with open("myfile.txt", "w") as file:
    file.write("This da first line")
    file.write("This da second line")
    file.write("This da third line")


# Opens the file in read mode and prints the line:
with open("myfile.txt", "r") as file:
    for i in range(3):
        lines = file.readline()
        print(lines)

# Deletes the file
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
