# Initial Enumeration and Automated Tools

1. [System Enumeration](#system-enumeration)
2. [User Enumeration](#user-enumeration)
3. [Network Enumeration](#network-enumeration)
4. [Password Hunting](#password-hunting)
5. [AV Enumeration](#av-enumeration)
6. [Automated Enumeration Tools](#automated-enumeration-tools)

## System Enumeration

* This is the stage where we have a reverse shell, and we need to enumerate the complete system for clues.

```shell
#from Meterpreter shell to Windows cmd
shell

systeminfo

#extract particular info
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"

hostname

wmic qfe
#check patches

wmic qfe get Caption,Description,HotFixID,InstalledOn
#filters info

wmic logicaldisk get caption,description,providername
#list drives
```
* Example: running `systeminfo` on a machine

```
c:\windows\system32\inetsrv>systeminfo
systeminfo

Host Name:                 DEVEL
OS Name:                   Microsoft Windows 7 Enterprise 
OS Version:                6.1.7600 N/A Build 7600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          babis
Registered Organization:   
Product ID:                55041-051-0948536-86302
Original Install Date:     17/3/2017, 4:17:31 
System Boot Time:          13/11/2022, 11:14:49 
System Manufacturer:       VMware, Inc.
System Model:              VMware Virtual Platform
System Type:               X86-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: x64 Family 23 Model 49 Stepping 0 AuthenticAMD ~2994 Mhz
BIOS Version:              Phoenix Technologies LTD 6.00, 12/12/2018
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             el;Greek
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC+02:00) Athens, Bucharest, Istanbul
Total Physical Memory:     3.071 MB
Available Physical Memory: 2.455 MB
Virtual Memory: Max Size:  6.141 MB
Virtual Memory: Available: 5.530 MB
Virtual Memory: In Use:    611 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    HTB
Logon Server:              N/A
Hotfix(s):                 N/A
Network Card(s):           1 NIC(s) Installed.
                           [01]: vmxnet3 Ethernet Adapter
                                 Connection Name: Local Area Connection 3
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 10.10.10.5
                                 [02]: fe80::58c0:f1cf:abc6:bb9e
                                 [03]: dead:beef::10d5:9590:d613:ebd5
                                 [04]: dead:beef::58c0:f1cf:abc6:bb9e
```
## User Enumeration

```shell
#in windows cmd
whoami

whoami /priv
#privileges
#certain privileges can be enabled and misused

whoami /groups
#check for administrative groups

net user
#users on machine

net user babis
#get info about user

net localgroup

net localgroup administrators
```

## Network Enumeration

```shell
ipconfig

ipconfig /all

arp -a
#check arp tables

route print
#check routing tables

netstat -ano
#check listening ports
```

## Password Hunting

```shell
findstr /si password *.txt *.config *.ini
#find the word 'password' in txt files in particular directory
#we can use PayloadAllTheThings payloads for password hunting
```

## AV Enumeration

```shell
sc query windefend
#service control
#check windows defender

sc queryex type= service
#show all services
#check for AVs

netsh advfirewall firewall dump
#firewall enum
netsh firewall show state

netsh firewall show config
```

## Automated Enumeration Tools

* Executables:

  * [winPEAS.exe](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)
  * [Seatbelt.exe](https://github.com/GhostPack/Seatbelt) (compile)
  * [Watson.exe](https://github.com/rasta-mouse/Watson) (compile)
  * [SharpUp.exe](https://github.com/GhostPack/SharpUp) (compile)

* PowerShell

  * [Sherlock.ps1](https://github.com/rasta-mouse/Sherlock)
  * [PowerUp.ps1](https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc)
  * [jaws-enum.ps1](https://github.com/411Hall/JAWS)

* Others:

  * [windows-exploit-suggester.py](https://github.com/AonCyberLabs/Windows-Exploit-Suggester) (run locally)
  * [Exploit Suggester](https://www.rapid7.com/blog/post/2015/08/11/metasploit-local-exploit-suggester-do-less-get-more/) (Metasploit)

```shell
#exploring enumeration tools when we cannot upload executables or files

#in Meterpreter shell
#exploit suggester
run post/multi/recon/local_exploit_suggester

#shell
shell

systeminfo
#copy sysinfo to a file sysinfo.txt

#in attacker machine
#update windows-exploit-suggester
python2 windows-exploit-suggester.py --update
#note database .xls file

pip2 install --user xlrd==1.1.0

python2 windows-exploit-suggester.py --database 2022-10-27-mssb.xls --systeminfo samplesysinfo.txt
#this gives us vulnerabilities list
```
