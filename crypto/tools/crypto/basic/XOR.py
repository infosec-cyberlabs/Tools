import sys

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "This program XORs 2 hex numbers"
        print "XOR [hex number] [hex number]"
        exit()

a = list(sys.argv[1])
b = list(sys.argv[2])
c = range(len(a))
for i in range(len(a)):
	c[i] = str(hex(int(a[i],16)^int(b[i],16))).replace("0x","")
print ''.join(c)

