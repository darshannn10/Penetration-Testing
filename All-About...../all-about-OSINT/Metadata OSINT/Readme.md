# Metadata OSINT

### Metagoofil

**Github:** [https://github.com/opsdisk/metagoofil](https://github.com/opsdisk/metagoofil)

Metagoofil is a tool for extracting metadata of public documents (pdf,doc,xls,ppt,etc) available in the target websites. This information could be useful because you can get valid usernames, people names, for using later in brute force password attacks (vpn, ftp, webapps), the tool will also extracts interesting "paths" of the documents, where we can get shared resources names, server names, etc. [\[Source\]](https://github.com/exiftool/exiftool#readme)

```bash
metagoofil -d <Domain> -t <FileExtension> -o <DestinationFolder>
```



The collected files can then be run alongside `Exiftool` to extract meta data information.

### Exiftool

**Github:** [https://github.com/exiftool/exiftool](https://github.com/exiftool/exiftool)

Exiftool is an command line application used to read and write meta information for a large variety of files.

Below is a wild card execution on PDF files. As per the image we can see a large amount of information that has been pulled from the PDF file.

```bash
exiftool -r *.pdf as
```


Grep can be used to pull only information we are interested in. This is a better suited option when dealing with a large amount of files.

```
exiftool -r *.pdf | egrep -i "Author|Creator|Email|Producer|Template" | sort -u
```


A large amount of information has been redacted from the search results purposely by myself. However, the results show the documents have been created by multiple out of date software.

We are also able to see authors names and usernames which can then be used to correlate email address.

This kind of information can also be correlated with database breaches to potentially discover plaintext passwords for existing users.

## Web Tools

### MetaData2Go

**URL:** [https://www.metadata2go.com/](https://www.metadata2go.com)
