# Tools

> Tools for the CTFs

## Commands CheatSheet
+ [CLI Cheatsheet](https://github.com/WebDevStudios/CLI-Cheat-Sheet)
+ [linux](https://ryanstutorials.net/linuxtutorial/)
+ [pipe](http://www.linfo.org/pipes.html)


## Binary exploitation/reversing

+ [IDA](https://www.hex-rays.com/products/ida/index.shtml) (Demo, if not Pro)
+ [gdb](https://www.gnu.org/software/gdb/)
+ [PEDA](https://github.com/longld/peda) - makes gdb far more usable
+ [qira](http://qira.me/) - if you can get it to work & understand it
+ [checksec](https://github.com/slimm609/checksec.sh) - peda can give the same info though
+ [pwntools](https://pwntools.readthedocs.io/en/stable/) - makes pwning easier
+ [radare2](https://github.com/radare/radare2) - reverse engineering framework
+ [angr](https://github.com/angr/angr) - a binary analysis framework with a great symbolic execution engine
+ [fupy](https://github.com/gdelugre/fupy) - fast and dirty python decompiler
+ [JD-GUI](https://github.com/java-decompiler/jd-gui) - java decompiler
+ [Java Decompilers](http://www.javadecompilers.com) - Online decompiler for Java and Android APKs
+ [syms2elf](https://github.com/danigargu/syms2elf) - A plugin for Hex-Ray's IDA Pro and radare2 to export the symbols recognized to the ELF symbol table 
+ [Objdump](https://linux.die.net/man/1/objdump)

## Cryptography

+ [Rumkin ciphers](http://rumkin.com/tools/cipher/) - multiple (ancient) crypto stuff
+ [quipqiup](https://quipqiup.com/) - solving cryptograms
+ [xortool](https://github.com/hellman/xortool) - solving multi-byte xor cipher
+ [rsatool](https://github.com/ius/rsatool) - to calculate rsa params
+ [featherduster](https://github.com/nccgroup/featherduster) -  An automated, modular cryptanalysis tool
+ [attackrsa](https://github.com/rk700/attackrsa) -  An all-in-one tool including many common attacks against RSA problems in CTF
+ [RsaCTFtool](https://github.com/sourcekris/RsaCtfTool) - An automated tool to crack public keys of rsa using various standard techniques
+ [Untwister](https://github.com/altf4/untwister) - A seed recovery tool for various PRNGs
+ [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) - A tool for Breaking PkZip-encryption
+ [Cyberchef](https://gchq.github.io/CyberChef/) - encoding & decoding
+ [Online substitution cypher solver](https://www.guballa.de/substitution-solver)

## Forensics
+ [Foremost](http://foremost.sourceforge.net/) - recover hidden files
+ [Binwalk](https://github.com/ReFirmLabs/binwalk) - find offsets of files which are concatenated contiguously
+ [Autopsy](https://github.com/sleuthkit/autopsy) - find deleted files from harddisk dumps
+ [Wireshark](https://www.wireshark.org/) - analyze network captures
+ [Stegsolve](http://www.ww.caesum.com/handbook/Stegsolve.jar)
+ [Cloudshark](https://www.cloudshark.org) - Analyze network captures online
+ [John The Ripper](http://www.openwall.com/john/) - password cracking tool
+ [Stegosaurus](https://bitbucket.org/jherron/stegosaurus/src) - tool that allows embedding arbitrary payloads in Python bytecode (pyc or pyo) files
+ [Audacity](http://sourceforge.net/projects/audacity/) - Analyze sound files (mp3, m4a, whatever)
  - `apt-get install audacity`
+ [bkhive and samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/) - Dump SYSTEM and SAM files
  - `apt-get install samdump2 bkhive`
+ [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE Editor
+ [Exif Tool](http://www.sno.phy.queensu.ca/~phil/exiftool/) - Read, write and edit file metadata
+ [extundelete](http://extundelete.sourceforge.net/) - Used for recovering lost data from mountable images
+ [Foremost](http://foremost.sourceforge.net/) - Extract particular kind of files using headers
  - `apt-get install foremost`
+ [fsck.ext4](http://linux.die.net/man/8/fsck.ext3) - Used to fix corrupt filesystems
+ [NetworkMiner](http://www.netresec.com/?page=NetworkMiner) - Network Forensic Analysis Tool
**run: `mono NetworkMiner.exe`**
+ [Google dork](https://whatis.techtarget.com/definition/Google-dork-query)
+ [steg online tool](http://stylesuxx.github.io/steganography/)
+ [Photorec from testdisk](https://www.cgsecurity.org/wiki/TestDisk) - recovering deleted file from disk `best tool`
+ [imago-forensics](https://github.com/redaelli/imago-forensics) - 
Imago is a python tool that extract digital evidences from images.



## Web exploitation
+ [Burpsuite](https://www.youtube.com/watch?v=IebZgk6P9Ss) 
+ [Burp-plugin](https://github.com/snoopysecurity/awesome-burp-extensions/blob/master/README.md)
+ [GitTools](https://github.com/internetwache/GitTools) - downloads exposed .git repo of vulnearable websites
+ [SQLMap](https://github.com/sqlmapproject/sqlmap) - automated sql injection
+ [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbar/) - indispensible addon for web exploitation in firefox
+ [CookieManager](https://addons.mozilla.org/en-US/firefox/addon/cookies-manager-plus/) - addon for firefox
+ [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) - add on for chrome.
+ [requests](https://github.com/requests/requests) - python library used for sending HTTP requests
+ [Wfuzz](http://www.edge-security.com/wfuzz.php) - to detect directories and pages on the server using common wordlists.
+ [XSS Payloads](https://github.com/nettitude/xss_payloads)
+ [Uglify](http://marijnhaverbeke.nl//uglifyjs)
+ [knockpy](https://github.com/guelfoweb/knock) - Knock Subdomain Scan
+ [Sublist3r](https://github.com/aboul3la/Sublist3r) - Fast subdomains enumeration tool for penetration testers.
+ [What CMS](https://whatcms.org/) - discover cms being used
+ [Striker](https://github.com/UltimateHackers/Striker) - Striker is an offensive information and vulnerability scanner. Mainly DNS
+ [XSStrike](https://somdev.me/XSStrike/) - Most advanced XSS scanner.
+ [joomscan](https://github.com/rezasp/joomscan) - OWASP Joomla Vulnerability Scanner Project [Owasp Doc.](https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project)

+ [OWASP Zap](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) - alternative to burp
+ [Wfuzz](https://wfuzz.readthedocs.io/en/latest/) - fuzzer and discovery tool - allows the discovery of web content by using wordlists 
+ [Dirb/dirbuster](https://medium.com/tech-zoom/dirb-a-web-content-scanner-bc9cba624c86), [dirbuster](https://null-byte.wonderhowto.com/how-to/hack-like-pro-find-directories-websites-using-dirbuster-0157593/) - brute force directories and files names on web/application servers.
+ [Knockpy](https://github.com/guelfoweb/knock) - subdomain enum using wordlists.
+ [Sublist3r](https://github.com/aboul3la/Sublist3r) - Subdomain enumeration with the use of search engines or OSINT
+ [Seclists](https://github.com/danielmiessler/SecLists) - great lists for assessments, usernames, passwords, URLs, fuzzing strings,common directories/files/sub domains 
+ [Scrapy](https://scapy.readthedocs.io/en/latest/) - Web crawling framework that allows you to create your own web crawlers

+ [For CMS](https://wpscans.com/) - Wpscan, joomscan[2](https://github.com/rezasp/joomscan)
+ [For exploits](https://www.exploit-db.com/) - Use exploit-db
+ [can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) - a list of services and how to claim (sub)domains with dangling DNS records.


## Bruteforcers

*Tools used for various kind of bruteforcing (passwords etc.)*

+ [Ophcrack](http://ophcrack.sourceforge.net/) - Windows password cracker based on rainbow tables.


## Exploits

*Tools used for solving Exploits challenges*



## Others
+ [Web tools](https://github.com/AlexisAhmed/BugBountyTools/blob/master/Tools.md)


+ [Bug Bounty Blogs](https://github.com/djadmin/awesome-bug-bounty.git) - 
A comprehensive curated list of available Bug Bounty & Disclosure Programs and Write-ups.

