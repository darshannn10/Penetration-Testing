# Username OSINT

Usernames can be used to correlate activity and information between multiple platforms. If we are hunting a particular person and have knowledge of a username and they are on Reddit, for example they may have provided information recently or in the past that, might narrow down who they are (Posts about car issues or local activities in particular city).

In some cases, where an email address can be linked to a username, we may be able to pull breached passwords from recent breaches and perform credential stuffing against the username, across multiple platforms.

Usernames can be searched with the web tools shown on this page. A couple of examples have been shown below.

### InstantUsername



### NameCheckup


### Sherlock

Sherlock is an excellent terminal based tool for hunting usernames down across multiple social media sites (323 at the time of writing):

**Github:** [https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

**Supported Sites:** [https://github.com/sherlock-project/sherlock/blob/master/sites.md](https://github.com/sherlock-project/sherlock/blob/master/sites.md)

```bash
sudo apt install sherlock
```

The following commands can be used to search using Sherlock:

```bash
# For a single user
sherlock <User>

# For multiple users
sherlock <User1> <User2> <User3>

# Make requests over TOR
sherlock -t <User>
```


## Resources

* **InstantUsername:** [https://instantusername.com](https://instantusername.com/#/)
* **NameCheckup:** [https://namecheckup.com/](https://namecheckup.com)
* **NameChk:** [https://namechk.com/](https://namechk.com)
* **WhatsMyName:** [https://whatsmyname.app/](https://whatsmyname.app)
