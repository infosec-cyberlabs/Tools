import sys
import numpy
import operator

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program detects a AES-128 ECB mode encrypted ciphertext from a file with a list of ciphertexts"
        print "AES128ECBdetect [file]"
        exit()

stds = []
cypherText = []
f = open(sys.argv[1], 'r')
for line in f:
	cypherText.append(line)
	chars = list(str(line).replace('\n','')[::-1])
	options = [0]*(int('FF',16)+1)
	for i in range(len(chars)/2):
		options[int(chars[(2*i)+1] + chars[2*i],16)] = options[int(chars[(2*i)+1] + chars[2*i],16)] + 1
	stds.append(numpy.std(options))
index = [i for i, x in enumerate(stds) if x == max(stds)]
for i in index:
	print i
	print cypherText[i]
	print stds[i]
