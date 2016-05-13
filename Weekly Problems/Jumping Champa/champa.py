def jumping(testcases):
    for a in xrange(testcases):
        N,Q = map(int, raw_input().split())
        H = map(int, raw_input().split())
        cost = 0
        Hlen = len(H)
        if Hlen > 1:
            H = sorted(H)
            for i in xrange(1,Hlen):
                cost+=Q*abs(H[i-1]-H[i])
        print cost
            
if __name__ == "__main__":
    jumping(int(raw_input()))
