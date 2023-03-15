#!/bin/bash
#Ops301d6: Code Challenge-01

#Author: Justin 'Sage' Tabios

#Purpose: Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename




cp /var/log/syslog ./
filename="syslog"

datetime=_$(date +%Y-%m-%d_%H-%M-%S)
new_filename="${filename}_${datetime}"

cp "$filename" "$new_filename"
rm "syslog"
#End
