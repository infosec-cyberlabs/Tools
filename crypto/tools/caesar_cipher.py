#!/usr/bin/env python

import string
import collections

c = 'ny_nx_tsq3_zumnqq_kwtr_mjwj_68b955abaa'

def caesar( rotate_string, number_to_rotate_by ):

	# upper = collections.deque( string.ascii_uppercase )
	lower = collections.deque( string.ascii_lowercase + string.digits ) 

	# upper.rotate( number_to_rotate_by )
	lower.rotate( number_to_rotate_by )

	lower = ''.join(list(lower))

	return rotate_string.translate( string.maketrans(string.ascii_lowercase + string.digits, lower) )


for i in range(26):
	print i, '|', caesar(c, i)
