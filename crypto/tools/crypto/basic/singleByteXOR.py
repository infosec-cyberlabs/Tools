import sys
import Crypto.Util.number

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program breaks a single byte key XOR encrypted ciphertext"
        print "singleByteXOR [ciphertext]"
        exit()

a = list(sys.argv[1])
b = range(len(a)/2)
results = []
score = []
for i in range(int('ff',16)):
	unreadable = 0
	notNormal = 0
	for j in range((len(a)/2)):
		b[j] = hex(int(a[(2*j)]+a[(2*j)+1],16)^i)
		if (
			not(
				(47 < int(b[j],16) and int(b[j],16) < 58) or
				(64 < int(b[j],16) and int(b[j],16) < 91) or
				(96 < int(b[j],16) and int(b[j],16) < 123) or
				(32 == int(b[j],16))
			) 
		):
			if not(31 < int(b[j],16) and int(b[j],16) < 127):
				unreadable = unreadable + 1
			else:
				notNormal = notNormal + 1
	results.append(Crypto.Util.number.long_to_bytes(int(''.join(b).replace('0x',''),16)))
	score.append(unreadable * 10 + notNormal)
index = [i for i, x in enumerate(score) if x == min(score)]
answer = []
for i in range(len(index)):
	print "Key: " + hex(index[i])
	print "Score: " + str(score[index[i]])
	print "Msg: " + results[index[i]]
