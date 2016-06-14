import math

def primesieve(ceiling):
    is_prime = [True for i in range(ceiling)]
    for i in xrange(2,int(math.sqrt(ceiling))+1):
        if is_prime[i] is True:
            j,k = i**2, 1
            for j in xrange(i*i, ceiling, i):
                is_prime[j] = False
    return [i for i in xrange(2,ceiling) if is_prime[i] == True]  

def winner(weight):
    primes = primesieve(weight)
    for p in primes:
        if weight-p in primes:
            return "Deepa"
    return "Arjit"

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        #print winner(int(raw_input()))
        #Goldbach's conjecture 
        #(any even number over 2 is the sum of 2 primes)
        if int(raw_input())>2: print "Deepa"
        else: print "Arjit"
