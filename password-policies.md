# Steps for password and account policy setting for Linux
### Note: To make changes on a Debian based system (kali-Linux, Ubuntu, etc) you’ll need to be root or you’ll have to use the `sudo` command for every command you execute.
1. <ins>Adding a new user</ins>

```
sudo useradd 'username'
```

2. <ins>Adding `new user’s` password </ins> 
```
sudo passwd `username`
```
3. <ins>Setting up `password length` policy</ins>

> Usually, the password and authentication-related configuration files are stored in /etc/pam.d/ directory in Debian-based systems

a. The password policies are defined in /etc/pam.d/common-password file. Before making any changes in it, backup this file, just in case.

```
sudo cp /etc/pam.d/common-password /etc/pam.d/common-password.bak
```

  b. To set minimum password length, edit /etc/pam.d/common-password file:
```
sudo nano /etc/pam.d/common-password
```

  c. Find the following line:
```
password [success=2 default=ignore] pam_unix.so obscure sha512
```
  d. And add an extra word: minlen=8 at the end. Here I set the minimum password length as 8. It should now look like this

```
password [success=2 default=ignore] pam_unix.so obscure sha512 minlen=8
```

e. Save and close the file. Now the users can't use less than 8 characters for their password.


4. <ins>Setting up `password complexity` policy</ins>
> This setting enforces how many classes, i.e upper-case, lower-case, and other characters, should be in a password.

a. First install password quality checking library using command:
```
sudo apt install libpam-pwquality
```

b. Then, edit `/etc/pam.d/common-password` file:
```
sudo nano /etc/pam.d/common-password
```

c. To set `at least one upper-case` letters in the password, add a word `ucredit=-1` at the end of the following line.
```
password        requisite                       pam_pwquality.so retry=3 ucredit=-1

```

![pam](https://user-images.githubusercontent.com/87711310/211911519-889e485a-ea9c-48fb-bb24-88ca1c166053.jpg)

d. Set at least one lower-case letters in the password as shown below.

```
password        requisite                       pam_pwquality.so retry=3 dcredit=-1
```

e. Set at least other letters in the password as shown below.
```
password        requisite                       pam_pwquality.so retry=3 ocredit=-1
```

f. You can also set the minimum/maximum number of allowed classes in the password. The following example shows the minimum number of required classes of characters for the new password:

```
password        requisite                       pam_pwquality.so retry=3 minclass=2
```

5. <ins>Setting up `password expiration` policy</ins>
> We are going to set the following policies.

- Maximum number of days a password may be used.
- Minimum number of days allowed between password changes.
- Number of days warning given before a password expires.

a. To set this policy, edit:
```
sudo nano /etc/login.defs
```
b. Set the values as per your requirement.
```
PASS_MAX_DAYS 100
PASS_MIN_DAYS 0
PASS_WARN_AGE 7
```
As you see in the above example, the user should change the password once in every 100 days and the warning message will appear 7 days before password expiration.

c. To set `maximum number of days between password change` to existing users, you must run the following command:
```
sudo chage -M <days> <username>
```

c. To set minimum number of days between password change, run:
```
sudo chage -m <days> <username>
```

d. To set warning before password expires, run:
```
sudo chage -W <days> <username>
```

e. To display the password for the existing users, run:
```
sudo chage -l sk
```

An Example of combining all the commands: 
```
$ sudo chage -E 28/02/2023 -m 5 -M 90 -I 10 -W 10 sk
```

The above command will set password of the user 'sk' to expire on 28/02/2023. Also the the minimum number days between password change is set 5 days and the maximum number of days between password changes is set to 90 days. The user account will be locked automatically after 10 days and It will display a warning message for 10 days before password expiration.


5. <ins>Forbidding previously used passwords on the system</ins>
> You can limit the users to set a password which is already used in the past. To put this in layman terms, the users can't use the same password again.

a. edit `/etc/pam.d/common-password` file with the following command:
```
sudo nano /etc/pam.d/common-password
```

b. Find the following line and add the word 'remember=5' at the end:
```
password        [success=2 default=ignore]      pam_unix.so obscure use_authtok try_first_pass sha512 remember=5
```

Change value of remember according to your needs.
