# Privilege Escalation Checklist

## System Information

Kernal information

```
uname -a
```

Operating System Information

```
cat /etc/issue
cat /etc/*-release
```

view $PATH

```
echo $PATH
```

## Network Information

View IP configuration information

```
ifconifg -a
```

Print current network routes

```
route -n
```

Check DNS resolver

```
cat /etc/resolv.conf
```

View ARP table

```
arp -en
```

> List all active TCP and UDP connections

Netstat
```
netstat -auntp
```

ss
```
ss -twurp
```

Dump clear text PSK keys from the Network manager.

```
cat /etc/NetworkManager/system-connections/* |grep -E "^id|^psk"
```

## User Information

Current user
```
id
```
From `/etc/passwd`  
```
grep $USER /etc/passwd
```


Last logged on

```
lastlog | grep -v '**Never logged in**' 
```

Currently logged on user

```
w
```

All users with UID and GUID Information

```
for user in $(cat /etc/passwd | cut -f1 -d ":"); do id $user; done
```

List all root accounts

```
cat /etc/passwd |cut -f1,3,4 -d":" | grep "0:0" |cut -f1 -d":" |awk '{print $1}'
```

## Running Processes

List running processes

```
ps auxwww
```

Processes running as root

```
ps -u root
```

Processes running as current user

```
ps -u $USER
```



## File and Folder permissions

Can we read Shadow?

```
cat /etc/shadow
```

Find Sticky bit

```
find / -perm -1000 -type d 2>/dev/null
```

Find SUID

```
find / -perm -u=s -type f 2>/dev/null 
```

Find SGID

```
find / -perm -g=s -type f 2>/dev/null
```

World Writeable files

```
find -perm -2 type -f 2>/dev/null   
```

List configuration files in /etc/

```
ls -al /etc/*.conf
```

Grep for interesting keywords in configuration files

```
grep 'pass*' /etc/*.conf 2> /dev/null
grep 'key' /etc/*.conf 2> /dev/null
grep 'secret' /etc/*.conf 2> /dev/null
```

Can we list the contents of root/?

```
ls -als root/
```

Can we read other users history files?

```
find /* -name *.*history* -print 2> /dev/null 
```

## Cronjobs and scheduled tasks

```
cat /etc/crontab  
ls -als /etc/cron.*
```

Check for tasks that are run as root and are world writeable.

```
find /etc/cron* -type f -perm -o+w -exec ls -l {} \; 
```

## Metasploit modules

Post exploit enumeration

```
post/linux/gather/enum_configs
post/linux/gather/enum_system
post/linux/gather/enum_network
post/linux/gather/enum_psk
post/linux/gather/hashdump
post/linux/gather/openvpn_credentials
post/linux/gather/phpmyadmin_credsteal 
```
