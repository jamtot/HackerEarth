def cakes(NnK):
    N,K=map(int,NnK.split())
    Ns = map(int,raw_input().split())
    return  sum(sorted(
            [sum([int(bn) for bn in str(bin(n))[2:]]) for n in Ns], 
            reverse=True)[:K])

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print cakes(raw_input())
