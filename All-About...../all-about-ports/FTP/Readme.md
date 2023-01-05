# Port 21 | FTP

Identity hosts running FTP

```bash
nmap -sV -p 21 --open <IP>
```

Manual banner grab

```bash
telnet <IP> 21
nc <IP> 21 
```

All Nmap scripts.

```bash
nmap --script ftp-* -p 21 <IP>
```


Anonymous check with Metasploit

```
use auxiliary/scanner/ftp/anonymous
```


## Download all files from FTP

```bash
wget -m ftp://anonymous:anonymous@10.10.10.98
wget -m --no-passive ftp://anonymous:anonymous@10.10.10.98
```
