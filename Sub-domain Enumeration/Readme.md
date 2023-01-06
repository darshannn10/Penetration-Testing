# Sub Domain Enumeration

## Google Dorking

Google dorks can be used to enumerate host subdomains. For example searching for Microsoft.com subdomains we can use the minus - symbol to tell Google to remove URL results for particular strings.


Every time a sub domain is found it can then be excluded from the next search

```
microsoft.com -www -docs -infrastructuremap
```



## Tools

### Amass

```bash
amass enum -d <domain>
```



### DNSRecon

```bash
# Quick brute force
dnsrecon -t brt -v -d <Domain>

# With Wordlist
dnsrecon -t brt -D <Wordlist> -v -d <Domain>
```



### Sublist3r

```bash
# Default Search
sublist3r -d <Domain> -v

# With brute force
```

### Wfuzz

```
wfuzz -c -f sub-fighter -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://love.htb" -H "Host: FUZZ.love.htb" --hl 125
```

## Web Tools

### Cert.sh

{% embed url="https://crt.sh" %}

Searching a domain name in Cert.sh can help identify when SSL Certificates have been issued to a particular domain and subdomains.



### DNSdumpster

[DNSdumpster](https://dnsdumpster.com) is a great tool for DNS and host enumeration. We even get a nice downloadable graph and can even export discovered hosts directly to `.xlsx`.



### VirusTotal

VirusTotal can be used to look up sub domains of a host: [https://www.virustotal.com/gui/home/search](https://www.virustotal.com/gui/home/search)

```
https://www.virustotal.com/gui/domain/<Domain>/relations
```


## Virtual Hosts

Some subdomains aren't always hosted in publicly accessible DNS results, such as development versions of a web application or administration portals.

Web servers can host multiple websites under the same IP. The web server is able to differentiate between requests by the value in the **Host** header of a request. It is possible to take advantage of this by fuzzing the host header for discovery.

### Fuff

```bash
ffuf -w <Wordlist> -H "Host: FUZZ.acmeitsupport.thm" -u <IP>
```
