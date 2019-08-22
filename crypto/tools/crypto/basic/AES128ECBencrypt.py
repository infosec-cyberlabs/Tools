import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program encrypts plaintext using a AES-128 in ECB mode given the key and returns the base64"
        print "AES128ECBencrypt [key] [text]"
        exit()

msg = sys.argv[2]
key = sys.argv[1]
a = AES.new(key, 1)#, iv)
while not(len(msg) %16 == 0):
	msg = msg + " "
print base64.b64encode(a.encrypt(msg))
