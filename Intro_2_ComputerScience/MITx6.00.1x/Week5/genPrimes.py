def genPrimes():
    primes = []
    lastPrime = 1
    
    while True:
        lastPrime += 1
        for p in primes:
            if lastPrime % p == 0:
                break
            else:
                primes.append(lastPrime)
                yield lastPrime
 