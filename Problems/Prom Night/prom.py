def dance():
    MN=map(int,raw_input().split())
    M,N=MN[0],MN[1]
    Mlist=map(int,raw_input().split())
    Nlist=map(int,raw_input().split())
    if M>N: return "NO"
    else:
        Mlist=sorted(Mlist)
        Nlist=sorted(Nlist)
        for i in xrange(M):
            if Mlist[i]<Nlist[i]:
                return "NO"
        else:
            return "YES"

    
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print dance()
