#!/usr/bin/env python
import sys
import Crypto.Util.number
import base64

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program breaks a reapeating XOR encrypted ciphertext encoded in base64 from a file"
        print "breakRepeatKeyXOR [file]"
        exit()

def singleByteXOR(input):
	a = list(input)
	b = range(len(a))
	results = []
	score = []
	for i in range(int('ff',16)):
		unreadable = 0
		notNormal = 0
		for j in range((len(a))):
			b[j] = hex(ord(a[j])^i)
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
	returnArray = []
	for i in range(len(index)):
		returnArray.append([hex(index[i]), float(score[index[i]])/len(input), results[index[i]]])
	return returnArray

def hammingDist(a, b):
	msg = list(b)
	key = list(a)
	results = []
	ans = 0
	for i in range(len(msg)):
		results.append(hex(ord(msg[i])^ord(key[i%len(key)])))
	for j in list(str(bin(int(''.join(results).replace("0x",""),16))).replace("0b","")):
		if j == '1':
			ans = ans + 1
	return ans

def decryptXOR(a, b):
	msg = list(b)
	key = list(a)
	results = []
	for i in range(len(msg)):
		results.append(str(hex(ord(msg[i])^ord(key[i%len(key)]))).replace("0x",""))
		if len(str(results[i])) < 2:
			results[i] = "0" + str(results[i]) 
	print Crypto.Util.number.long_to_bytes(int(''.join(results).replace('0x',''),16))

f = open(sys.argv[1], 'r')
fileText = f.read().replace("\n","")
c = base64.b64decode(fileText)
keysize = range(1,41)
keyscores = []
for size in keysize:
	avg = 0
	for i in range((len(c)/size)-3):
		avg = avg + float(hammingDist(c[(size*i):(size*(i+1))],c[(size*(i+1)):(size*(i+2))]))/size
	keyscores.append(avg/((len(c)/size)-3))
	#keyscores.append(float(hammingDist(c[:size],c[size:size*2]))/size)
	#keyscores.append(float(hammingDist(c[:size],c[size:size*2])+hammingDist(c[size:size*2],c[size*2:size*3]))/(2*size))
index = [i for i, x in enumerate(keyscores) if x == min(keyscores)]
for i in range(len(keyscores)):
	print "Keylength: " + str(i + 1) + "\t\tScore: " + str(keyscores[i])
for i in range(len(index)):
	print "Recomended: " + str(index[i] + 1)
keylength = input('Choose a key length: ')
charTexts = []
keyscores = []
text = []
for i in range(keylength):
	charTexts.append("")
for chari in range(len(c)):
	charTexts[chari%keylength] = charTexts[chari%keylength] + c[chari:chari+1]
keyopt = []
for charText in charTexts:
	charopt = []
	output = singleByteXOR(charText)
	for keyChar in output:
		[keychar, score, charsPT] = keyChar
		charopt.append(chr(int(keychar,16)))
	keyopt.append(charopt)
keys = [""]
for char in keyopt:
	if len(char) < 2:
		for i in range(len(keys)):
			keys[i] = keys[i] + char[0]
	else:
		length = len(keys)
		for i in range(len(char)):
			if not(i == len(char)-1):
				for j in range(length):
					keys.append(keys[j] + char[i])
			else:
				for j in range(length):
					keys[j] = keys[j] + char[i]
print "Recommended Keys:"
for key in keys:
	print key
print "*Leave empty to try all keys*"
key = raw_input('Key: ')
if key == "":
	for key in keys:
		decryptXOR(key, c)
else:
	decryptXOR(key, c)
