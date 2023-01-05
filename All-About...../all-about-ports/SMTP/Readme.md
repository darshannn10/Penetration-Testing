# Port 25 | SMTP

Identify hosts running SMTP.

```bash
nmap -sV -p 25,465,587 <IP> --open
```

Identify available SMTP commands.

```
nmap --script smtp-commands -p25 <IP>
```

Those above script will identify all commands. The following below can be used to grep for methods to be used with `smtp-user-enum` for user identification.

```
nmap --script smtp-commands -p25 <IP> | grep -Eo 'VRFY|EXPN|RCPT'
```

With verified methods `smtp-user-enum` can be used to identify users from a given word list.

```
smtp-user-enum -U <Word-list> -M VRFY -t <IP>
```


### Metasploit

```
use auxiliary/scanner/smtp/smtp_enum
```

## Sending Emails

```bash
# mutt
echo "<Body>" | mutt -s "<Subject>" <Recipient> -r <Recipient> -a <Attachment>          

# SendEmail
sendEmail -t <Recipient> -f <SendingAddress> -s <IP> -u <Subject> -a <Attachment> 

# Swaks
swaks -s "<Server>"  -t "<Recipient>" -f "<FromAddress>" --header "Subject:" --body "" --attach <Attachment>
```
