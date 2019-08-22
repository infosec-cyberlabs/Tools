Bruteforce Cipher
=================

> John Hammond | October 2nd, 2016

----------------------------------


This tool runs through all of the possible "modes" for [`openssl`][openssl] to try and decrypt an encrypted file, when given a possible password.

This script was originally found through this writeup:
[`https://github.com/Beers4Flags/writeups/tree/master/hackit2016/network/australia-voice-of-the-future`](https://github.com/Beers4Flags/writeups/tree/master/hackit2016/network/australia-voice-of-the-future)

I have only modified it to make it a bit more of a universal tool.

Usage
---------

```
Usage:
    $0 -f ENCRYPTED_FILE -k KEY

Parameters:
    -f
        Specify the encrypted file that will be created and used for this server.
        
    -k
        Specify the suspected key that should decrypt the encrypted file (supplied with -f)

    -h
        Display this help message
```

[openssl]: https://www.openssl.org/docs/manmaster/apps/openssl.html