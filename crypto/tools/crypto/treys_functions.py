def multiples(a, b):
	#input: 2 integers a and b
	#output: there multiples to fufil the euclidean algorithm equasion a*x + y*b = gcd
    if a == 0:
        return (0, 1)
    else:
        y, x = multiples(b % a, a)
        return (x - (b // a) * y, y)

def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y 

def modinv(n, mod):
	#input: a number and it's modulus
	#output: the modular inverse
	x, y = multiples(n, mod)
	return x % mod

def euclid(x, y):
	#input: 2 integers
	#output: the gcd as calcuated by the euclidean algorithm
	if y > x:
		z = y
		y = x	
		x = z
	if y == 0:
		return x
	else:
		return euclid(y, x % y)

def intsqrt(n):
	#input: a number
	#output: integer square root of the number using newton's meathod
	x = n
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

def hex2str(h):
	#input: a string
	#output: the hex representation of the string
	return bytearray.fromhex(h.replace('L','').replace("0x",'')).decode()

def bchcode():
	gen = raw_input("Enter a primitive polynomial in binary vector form: ")
	gen = list(str(gen))
	gen = [int(i) for i in gen]
	maxpow = 2**(len(gen)-1) -2
	print ' '*(len(gen) - 4) + "word | power of beta"
	print '-'*(len(gen) - 4) + "--------------------"
	print ' ' + '0'*(len(gen)-1) + " |     -1"
	beta = []
	for i in range(maxpow + 1):
		word = [1]
		for j in range(len(gen)-2):
			word.append(0)
		for j in range(i):
			word.insert(0,0)
			if word.pop() == 1:
				for k in range(len(word)):
					word[k] = (word[k] + gen[k])%2 
		word = [str(j) for j in word]
		print ' ' + ''.join(word) + " |      " + str(i)
		beta.append(word)
	print 
	print 
	print "Parity Check Matrix: "
	pcmat = []
	for i in range(maxpow + 1):
		print ''.join(beta[i]) + ''.join(beta[3*i % (maxpow + 1)])
		pcmat.append(beta[i] + beta[3*i % (maxpow + 1)])
	pcmat = [[int(j) for j in i] for i in pcmat]
	print 
	print 
	print "List of Codewords: "
	for i in range(int('1'*(maxpow+1),2)+1):
		msg = list(bin(i).replace("0b",''))
		while len(msg) < len(pcmat):
			msg.insert(0,'0')
		msg = [int(j) for j in msg]
		ansvec = []
		for i in range(len(pcmat[0])):
			element = 0
			for j in range(len(pcmat)):
				element = element + msg[j]*pcmat[j][i]
			ansvec.append(element)
		syndrome = [i%2 for i in ansvec]
		syndrome = [j % 2 for j in syndrome]
		if sum(syndrome) == 0:
			msg = [str(j) for j in msg]
			print ''.join(msg)
	msg = raw_input("Enter a message for error correction: ")
	while msg != '':
		msg = list(str(msg))
		beta = [[str(j) for j in i] for i in beta]
		while len(msg) < len(pcmat):
			msg.insert(0,'0')
		msg = [int(j) for j in msg]
		ansvec = []
		for i in range(len(pcmat[0])):
			element = 0
			for j in range(len(pcmat)):
				element = element + msg[j]*pcmat[j][i]
			ansvec.append(element)
		syndrome = [i%2 for i in ansvec]
		syndrome = [j % 2 for j in syndrome]
		s1 = -1
		s3 = -1
		syndrome = [str(j) for j in syndrome]
		for i in beta:
			if i == syndrome[:len(syndrome)/2]:
				s1 = beta.index(i)
		for i in beta:
			if i == syndrome[len(syndrome)/2:]:
				s3 = beta.index(i)
		syndrome = [int(j) for j in syndrome]
		msg = [str(j) for j in msg]
		if sum(syndrome) == 0:
			print "No error has occured.  Your message is " + ''.join(msg)
		elif syndrome[:len(syndrome)/2] == 0:
			print "Too many errors have occured.  Please retransmit."
		elif s1 != -1:
			if (3*s1) % (maxpow + 1) == s3:
				if msg[s1] == '1':
					msg[s1] = '0'
				else:
					msg[s1] = '1'
				print "One error has occured at position " + str(s1) + ". Your message is " + ''.join(msg)
			else:
				beta = [[int(j) for j in i] for i in beta]
				if s3 == -1:
					c = (s1*2) %(maxpow + 1)
				
				else:
					c1 = (s3-s1) %(maxpow + 1)
					c2 = (s1*2) %(maxpow + 1)
					cvector = []
					for j in range(len(beta[0])):
							cvector.append((beta[c1][j] + beta[c2][j]) % 2)
					for j in beta:
						if j == cvector:
							c = beta.index(j)
				b = s1
				roots = []
				for i in range(maxpow + 1):
					solution = []
					t1 = (i*2) %(maxpow + 1)
					t2 = (i+b) %(maxpow + 1)
					t3 = c %(maxpow + 1)
					for j in range(len(beta[0])):
						solution.append((beta[t1][j] + beta[t2][j] + beta[t3][j]) % 2)
					if sum(solution) == 0:
						roots.append(i)
				if len(roots) == 2:
					if msg[roots[0]] == '1':
						msg[roots[0]] = '0'
					else:
						msg[roots[0]] = '1'
					if msg[roots[1]] == '1':
						msg[roots[1]] = '0'
					else:
						msg[roots[1]] = '1'
					print "Two errors have occured at positions " + str(roots[0]) + " and " + str(roots[1]) + ". Your message is " + ''.join(msg)
				else:
					print "Too many errors have occured.  Please retransmit."
		else:
					print "Too many errors have occured.  Please retransmit."
		try:
			msg = raw_input("Enter another message for error correction: ")
		except SyntaxError:
			msg = ''

#bchcode()
