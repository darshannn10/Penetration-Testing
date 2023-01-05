# Social Media OSINT Tools

## Facebook

### Fuck Facebook (TM)

URL: [https://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.pet/](https://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.pet/)

## Instagram

### OSintgram

**Github:** [https://github.com/Datalux/Osintgram](https://github.com/Datalux/Osintgram)

**Install:** [https://github.com/Datalux/Osintgram#installation-%EF%B8%8F](https://github.com/Datalux/Osintgram#installation-%EF%B8%8F)

```
git clone https://github.com/Datalux/Osintgram.git
pip install -r requirements.txt
```

Once installed ensure your sock puppet Instagram account details are entered into `/config/credentils.ini`.

**Usage:** [https://github.com/Datalux/Osintgram#tools-and-commands-](https://github.com/Datalux/Osintgram#tools-and-commands-)

## Reddit

### Reddit-Analyzer

**Github:** [https://github.com/sshell/reddit-analyzer](https://github.com/sshell/reddit-analyzer)

**Install**

```bash
git clone https://github.com/sshell/reddit-analyzer.git

# If missing module ascii_graphs
pip install ascii_graphs
```

**Usage**

```bash
python3 reddit-analyzer.py "<Username>"
```



## Snapchat

### Snapchat Username Checker

**Github:** [https://github.com/SudoSuu/SnapchatUsernameChecker](https://github.com/SudoSuu/SnapchatUsernameChecker)

**Install:** [https://github.com/SudoSuu/SnapchatUsernameChecker#installing](https://github.com/SudoSuu/SnapchatUsernameChecker#installing)

```bash
git clone https://github.com/SudoSuu/SnapchatUsernameChecker.git
cd SnapchatUsernameChecker
pip3 install -r requirements.txt
python3 snapchat.py
```


## Twitter

### Twint

**Github:** [https://github.com/twintproject/twint](https://github.com/twintproject/twint)

**Install**

```bash
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
```

**Usage:** [https://github.com/twintproject/twint#cli-basic-examples-and-combos](https://github.com/twintproject/twint#cli-basic-examples-and-combos) **And** [https://github.com/twintproject/twint#followersfollowing](https://github.com/twintproject/twint#followersfollowing)

Better usage examples are shown above. However, some are shown below.

```bash
# Scrape tweets from a user
twint -u <User>

# Scrape keywords from a specific user
twint -u <User> -s <Word>

# Scrape keywords from verified users
twint -s "Doge" --verified

# Scrape followers from a specific user
twint -u <User> --followers

# Scrape who a specific user is following
twint -u <User> --following

# Scrape tweets from a specified date
twint -u <User> --since 2015-12-20

# Output results to a CSV file.
twint -u <User> -o <File.csv> --csv
```


