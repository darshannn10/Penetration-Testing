# Password OSINT

## Local Database (Linux)

Download the 3.2 billion record list

**COMB:** [https://github.com/samokosik/COMB](https://github.com/samokosik/COMB)

Once the torrent is downloaded. Use the following password to unzip:

```
+w/P3PRqQQoJ6g
```

### Breach-Parse

Once the database has been downloaded we can use Breach-Parse to pull targeted information from the database.

**Breach Parse:** [https://github.com/hmaverickadams/breach-parse](https://github.com/hmaverickadams/breach-parse)

Following the Breach-Parse install instructions we can then run Breach-Parse against the database downloaded earlier.

```bash
# Search for all results in a domain
breach-parse <Domain> Domain.txt "/media/sf_CompilationOfManyBreaches/data"

# Search for a specific email address
breach-parse <Example@Outlook.com> Email.txt "/media/sf_CompilationOfManyBreaches/data"
```

```bash
breach-parse @example.com Example.txt "/media/sf_CompilationOfManyBreaches/data"  
```

Breach-Parse will then create three separate files as shown below. We are then able to read the contents of the master file to read both breached email addresses and plain text passwords.


## Local Database (Windows)

Download the 3.2 billion record list

**COMB:** [https://github.com/samokosik/COMB](https://github.com/samokosik/COMB)

Once the torrent is downloaded. Use the following password to unzip (Use 7zip):

```
+w/P3PRqQQoJ6g
```

### Notepad++

**Notepad++:** [https://notepad-plus-plus.org/downloads/](https://notepad-plus-plus.org/downloads/)

In Notepad++ select the pink folder icon to add a folder as a workspace. After adding the data folder from the COMB database we should see something similar as below.


We can then right click on the data folder and proceed with "Find in files". Allowing us to specify a search query on the entire database.


This will take some time to complete. However, once completed we should see a screen similar to this:


## Web Tools

### HaveIBeenPwned

**URL:** [https://haveibeenpwned.com/](https://haveibeenpwned.com)


We can see from the example above the account _example@microsoft.com_ has been involved in 21 breaches and 1 paste.

A little further down the page we can see what breaches they were and a little more information. Each listing will describe some details about the breach and what was leaked. In some cases, this may be only email addresses and in others, this could be plain text or hashes passwords with related email addresses.


In many of these cases it would be feasible to assume the related accounts database breaches are discoverable online whether free or paid for.

This site is a useful resource for blue team personnel as with a registered account it is possible to receive notifications for when specific accounts are found in future breaches. The blue team can also verify ownership of a domain and perform a domain wide search on breaches, as well as setup breach notifications for future leaks.

## Resources

**Dehashed:** [https://dehashed.com/](https://dehashed.com)

**WeLeakInfo:** [https://weleakinfo.to/v2/](https://weleakinfo.to/v2/)

**LeakCheck:** [https://leakcheck.io/](https://leakcheck.io)

**SnusBase**: [https://snusbase.com/](https://snusbase.com)

**Scylla (Hopefully soon):** [https://scylla.so/](https://scylla.so)

**HaveIBeenPwned:** [https://haveibeenpwned.com/](https://haveibeenpwned.com)

**ComboList:** [https://github.com/samokosik/COMB](https://github.com/samokosik/COMB)
