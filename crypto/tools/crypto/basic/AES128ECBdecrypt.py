import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program decrypts a AES-128 encrypted base64 ciphertext in ECB mode from a file"
        print "AES128ECBdecrypt [key] [file]"
        exit()

f = open(sys.argv[2],'r')
c = f.read()
key = sys.argv[1]
a = AES.new(key, 1)#, iv)
print base64.b64decode(c)
print a.decrypt(base64.b64decode(c))
