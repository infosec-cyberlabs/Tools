import sys

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program encrypts a message using a repeaking key and XOR encryption"
        print "encryptXOR [key] [msg]"
        exit()

msg = list(sys.argv[2])
key = list(sys.argv[1])
results = []
for i in range(len(msg)):
	results.append(str(hex(ord(msg[i])^ord(key[i%len(key)]))).replace("0x",""))
	if len(str(results[i])) < 2:
		results[i] = "0" + str(results[i]) 
print ''.join(results)
