def primesum(N, sumdict={}, primes=[2,3,5,7]):
    if N<2: return -1
    elif N in primes: return 1    
    elif N not in sumdict:
        least = float('inf') # infinity, I think

        # put stuff in here

        sumdict[N] = least
    return sumdict[N]

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        ans = primesum(int(raw_input()))
        if ans==float('inf'): print -1
        else: print ans
