#Ops301d6: Code Challenge-01

#Author: Justin 'Sage' Tabios

#Purpose: 

#referred to ChatGPT to frame the scripts
# Prompts user for input directory path
#!/bin/bash

echo "Please enter a directory path: "
read dir_path

if [ -d "$dir_path" ]; then
  echo "Directory exists"
else
  echo "Invalid directory path"
fi

# Prompts user for input permissions number
echo "Please enter a permissions number (e.g. 755): "
read permissions

if [[ $permissions =~ ^[0-7]{3}$ ]]; then
  chmod $permissions /path/to/file/or/directory
  echo "Permissions set to $permissions"
else
  echo "Invalid permissions number"
fi 
# Navigates to the directory input by the user and changes all files inside it to the input setting
#!/bin/bash

echo "Please enter a directory path: "
read dir_path

echo "Please enter a permissions setting (e.g. 755): "
read permissions

if [[ $permissions =~ ^[0-7]{3}$ ]] && [ -d "$dir_path" ]; then
  cd "$dir_path"
  find . -type f -exec chmod $permissions {} +
  echo "Permissions set to $permissions for all files in $dir_path"
else
  echo "Invalid input"
fi

# Prints to the screen the directory contents and the new perissions settings of settings of everything in the directory.
