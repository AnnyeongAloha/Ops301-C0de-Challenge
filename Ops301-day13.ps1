# Ops301 Daily Code Challenge Day-13 
# Author: Justin 'Sage' Tabios
# Date of revision: 29 Mar 2023

Purpose: Script creates AD user

Import-Module ActiveDirectory
New-ADUser -Name "Franz Ferdinand"  -SamAccountName "Franz.F" -UserPrincipalName "Franz Ferdinand" -AccountPassword (Read-Host -AsSecureString "solarwinds123") -Enabled $true
Get-ADUser Franz.F
