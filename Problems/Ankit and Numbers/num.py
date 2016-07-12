from itertools import combinations

# brute force
def powersetsum(N):
    S=range(1,N+1)
    return sum([sum([sum(combo) for combo in combinations(S, i)]) for i in S])

def pssum(N):
    return ((N*(N+1))/2)*(2**(N-1))

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        #print powersetsum(int(raw_input()))
        print pssum(int(raw_input()))
