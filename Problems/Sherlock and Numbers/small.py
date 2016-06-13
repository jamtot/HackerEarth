def pth(N,K,P): # too slow for the huge inputs
    A=set(map(int,raw_input().split()))
    try:
        return [x for x in range(1,N+1) if x not in A][P-1]
    except IndexError:
        return -1

def ppth(N,K,P):
    x=P
    e = map(int,raw_input().split())
    for i in xrange(K):
        if(e[i]<=x):
            x+=1
    if(P<=N-K):
        return x
    else:
        return -1

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        nkp = map(int,raw_input().split())
        print ppth(nkp[0],nkp[1],nkp[2])
