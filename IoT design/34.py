small_primes = set() 	# empty set
small_primes.add(2) 	# adding one element at a time
small_primes.add(3)
small_primes.add(5)
small_primes

small_primes.add(1) 	# Look what I’ve done, 1 is not a prime !
small_primes

small_primes.remove(1) 	# so let’s remove it
3 in small_primes 	#membership test

3 in small_primes

4 not in small_primes 		#negated membership test

small_primes.add(3) 	# trying to add 3 again
small_primes
# no change, duplication is not allowed
bigger_primes = set([5, 7, 11, 13]) 	# faster creation
small_primes | bigger_primes 		# union operator ‘|’

small_primes & bigger_primes 		# intersection operator ‘&’

small_primes - bigger_primes 		# difference operator ‘-‘