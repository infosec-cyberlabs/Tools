import sys
import Crypto.Util.number

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program detects and breaks a single byte key XOR encrypted ciphertext from a list of ciphertexts in a file"
        print "detectSBXOR [file]"
        exit()

def singleByteXOR(input):
	a = list(input)
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
		answer.append([hex(index[i]),score[index[i]],results[index[i]]])
	return answer

cypherText = []
ansList = []
scores = []
f = open(sys.argv[1], 'r')
for line in f:
	cypherText.append(line.replace('\n',''))
for i in range(len(cypherText)):
	answer = singleByteXOR(cypherText[i])
	for k in range(len(answer)):
		answer[k].append(i)
		answer[k].append(cypherText[i])
		ansList.append(answer[k])
		scores.append(answer[k][1])
finalAns = [i for i, x in enumerate(scores) if x == min(scores)]
for j in range(len(finalAns)):
	print "Key: " + ansList[finalAns[j]][0]
	print "Score (Low is good): " + str(ansList[finalAns[j]][1])
	print "Message: " + ansList[finalAns[j]][2]
	print "# in File: " + str(ansList[finalAns[j]][3])
	print "Cypher Text: " + ansList[finalAns[j]][4]
	print "\n"
