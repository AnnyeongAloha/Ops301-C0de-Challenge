#!/usr/bin/env python3
# Script: Ops301d6 Challenge-06
# Author: Justin 'Sage' Tabios

# Requirements:
# The Python module “os” must be utilized
# At least three variables must be declared in Python that contain results of bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:

# whoami
# cd $Home
# lshw -short




# How to use Linux/Bash commands within Python
# The Python module “os” must be utilized
import os

# Then use os.system to call any kind of bash command
# At least three variables must be declared in Python that contain results of bash operations
var1 = [os.system("whoami")]
var2 = [os.system("cd $Home")]
var3 = [os.system("lshw -short")]


# The Python function print() must be used at least three times
print (var1)
print (var2)
print (var3)
