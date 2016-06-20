def getminsum(a,b,c,N):
    #A,B=[],[]
    #A.append((a*c)%1000000007)
    #B.append((b*c)%1000000007)
    MODVAL=1000000007
    prevA=(a*c)%MODVAL
    prevB=(b*c)%MODVAL
    Amin1=[prevA,0]
    Bmin1=[prevB,0]
    Amin2=[MODVAL,-1]
    Bmin2=[MODVAL,-1]
    for i in xrange(1,N):
        #A.append((A[i-1]*a*b*c + A[i-1]*a*b + A[i-1]*a*c)%1000000007)
        #B.append((B[i-1]*b*c*a + B[i-1]*b*a + B[i-1]*b*c)%1000000007)
        curA=(prevA*a*b*c + prevA*a*b + prevA*a*c)%MODVAL
        curB=(prevB*b*c*a + prevB*b*a + prevB*b*c)%MODVAL
        if curA<Amin1[0]:
            Amin1[0]=curA
            Amin1[1]=i
        elif curA<Amin2[0]:
            Amin2[0]=curA
            Amin2[1]=i
        if curB<Bmin1[0]:
            Bmin1[0]=curB
            Bmin1[1]=i
        elif curB<Bmin2[0]:
            Bmin2[0]=curB
            Bmin2[1]=i
        prevA=curA
        prevB=curB
    if Amin1[1]!=Bmin1[1]:
        return Amin1[0]+Bmin1[0]
    else:
        if (Amin1[0]+Bmin2[0])<(Amin2[0]+Bmin1[0]):
            return Amin1[0]+Bmin2[0]
        else:
            return Amin2[0]+Bmin1[0]

if __name__ == "__main__":
    abc = map(int,raw_input().split())
    a,b,c=abc[0],abc[1],abc[2]
    N=int(raw_input())
    print getminsum(a,b,c,N)
