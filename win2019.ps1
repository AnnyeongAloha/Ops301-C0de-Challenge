#Install Active Directory Domain Services(ADDS)
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
#Restart Server
Restart-Computer -Force
----
#Promote server to Domain controller and ser domain
Write-Output
Intall-ADDSforest `
-CreateDnsDelegatio:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "Winthreshold" `
-DomainName "sunflow.com" `
-DomainNetbiosName "Sunflow" `
-ForestMode "WinThreshold `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootCompletion::$false `
-SysvolPath "C:\Windows\SYSVOL"
-Forece:$true
#Follow prompt to specify the Directory Services Restore MOde()DSRM
#Restart computer if not done by DC promotion
Restart-Computer -F
---
#Set Network adapter name and IP config
$adapterName="Ethernet"
$IPAddress="192.168.1.9"
$subnetMask="255.255.255.0"
$defaultGateway="192.168.1.1"
$dns1="192.168.1.1"
$dns2="8.8.4.4"
#Set Network adapter to use static IP
New-NetIPAddress -InterfaceAlias $adapterName -IPAddress $IPAddress
-PrefixLength 24 -DefaultGateway $defaultGateway
#Set subnetmask
New-NetIPAddress -InterfaceAlias $adapterName -InterfaceMetric 10
-IPV4Metric 10 -InterfaceIndex (Get-NetAdapter -InterfaceAlias
"Ethernet").ifIndex -AddressFamily IPV4 -PrefixLength 24 -SkipAsSource
$true
#Set DNS servers
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddress
($dns1, $dns2)
