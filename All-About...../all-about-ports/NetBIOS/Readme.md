# Ports 137 | 138 | 139 | NetBIOS

```markup
nmblookup -A <IP>
nbtscan <IP>/30 -v
sudo nmap -sU -sV -T4 --script nbstat.nse -p137 -Pn -n <IP>
nmap --script=msrpc-enum <IP>
```

### Metasploit

```markup
auxiliary/scanner/netbios/nbname
```
