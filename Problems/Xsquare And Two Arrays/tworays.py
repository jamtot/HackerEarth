def twoarrays(N,Q): 
    A=map(int,raw_input().split())
    B=map(int,raw_input().split())
    for i in xrange(Q):
        nLR = map(int,raw_input().split())
        a,L,R=nLR[0],nLR[1]-1,nLR[2]-1
        query = 0
        result = [None]*(R-(L-1))
        if a==1:
            result[::2]=A[L:R+1:2]
            result[1::2]=B[L+1:R+1:2]
        else:
            result[::2]=B[L:R+1:2]
            result[1::2]=A[L+1:R+1:2]
        print sum(result)
    

if __name__ == "__main__":
    N,Q = map(int,raw_input().split())
    twoarrays(N,Q)
