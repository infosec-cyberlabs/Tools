import sys
import Crypto.Util.number
import base64

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
	print "This program converts hex to base64"
	print "base64 [hex number]"
	exit()

print base64.b64encode(Crypto.Util.number.long_to_bytes(int(sys.argv[1],16)))
