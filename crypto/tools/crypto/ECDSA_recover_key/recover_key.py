def recover_key(c1,sig1,c2,sig2,pubkey):
      #using the same variable names as in:
      #http://en.wikipedia.org/wiki/Elliptic_Curve_DSA

      curve_order = pubkey.curve.order

      n = curve_order
      s1 = string_to_number(sig1[-48:])
      print "s1: " + str(s1)
      s2 = string_to_number(sig2[-48:])
      print "s2: " + str(s2)
      r = string_to_number(sig1[-96:--48])
      print "r: " + str(r)
      print "R values match: " + str(string_to_number(sig2[-96:--48]) == r)

      z1 = string_to_number(sha256(c1))
      z2 = string_to_number(sha256(c2))

      sdiff_inv = inverse_mod(((s1-s2)%n),n)
      k = ( ((z1-z2)%n) * sdiff_inv) % n
      r_inv = inverse_mod(r,n)
      da = (((((s1*k) %n) -z1) %n) * r_inv) % n

      print "Recovered Da: " + hex(da)

      recovered_private_key_ec = SigningKey.from_secret_exponent(da, curve=NIST384p)
return recovered_private_key_ec.to_pem()