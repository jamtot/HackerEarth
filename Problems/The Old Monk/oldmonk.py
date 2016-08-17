def binsearch(B,Ai,i,N):
    mid=0
    pos=0
    m=N-1
    while i<=m:
        mid=(i+m)/2
        if B[mid]<Ai:
            m=mid-1
        elif B[mid]>=Ai:
            pos=mid
            i=mid+1
    return pos

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        N=int(raw_input())
        A=map(int,raw_input().split())
        B=map(int,raw_input().split())
        ans=0
        for i in xrange(N):
            j=binsearch(B,A[i],i,N)
            ans=max(ans,j-i)
        print ans
        
