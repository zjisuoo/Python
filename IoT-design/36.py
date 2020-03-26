small_primes = frozenset( [2, 3, 5, 7] )
bigger_primes = frozenset( [5, 7, 11] )
small_primes.add(11) # we cannot add to a frozenset
small_primes.remove(2) # neither we can remove
small_primes & bigger_primes # intersect, union, etc. allowed
