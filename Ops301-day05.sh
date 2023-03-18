#!/bin/bash

#Script: Ops 301 Class 05 Ops Challenge Solution
#Author: Justin 'Sage' Tabios
#Date of latest revision: 17 Mar 2023
#Purpose: Create a bash script that display the size of log files, compresses and copies the log files to a backup directory with a timestamp.

# Source: ChatGPT, MarcoGPT
#Main

#Display the size of log files
echo "The size of the log files are:"
echo "/var/log/syslog: $(du -h /var/log/syslog | awk '{print $1}')"
echo "/var/log/wtmp: $(du -h /var/log/wtmp | awk '{print $1}')"

#Create variable for backup directory and timestamp
backupDir="/var/log/backups"
timestamp=$(date +%Y-%m-%d_%H%M%S)

#Create backup directory if it doesn't exist
if [ ! -d $backupDir ]; then
    mkdir $backupDir
fi

#Compress and copy log files to backup directory
echo "Compressing and copying log files to backup directory..."
gzip -c /var/log/syslog > $backupDir/syslog_$timestamp.gz
gzip -c /var/log/wtmp > $backupDir/wtmp_$timestamp.gz

#Display the size of the compressed log files
echo "The size of the compressed log files are:"
echo "$backupDir/syslog_$timestamp.gz: $(du -h $backupDir/syslog_$timestamp.gz | awk '{print $1}')"
echo "$backupDir/wtmp_$timestamp.gz: $(du -h $backupDir/wtmp_$timestamp.gz | awk '{print $1}')"

#Display size of original log files
echo "The size of the original log files are:"
echo "/var/log/syslog: $(du -h /var/log/syslog | awk '{print $1}')"
echo "/var/log/wtmp: $(du -h /var/log/wtmp | awk '{print $1}')"

#Clear log files
echo "Clearing log files..."
cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp
echo "Log files cleared."

#Exit becuase its elegant
exit 0

#End
