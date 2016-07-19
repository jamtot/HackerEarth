def moddable(N):
    seq=map(int,raw_input().split())
    if N==1:
        if seq[0]==0:
            return "YES"
        else: 
            return "NO"
    for i in xrange(N-1):
        while seq[i] > 0:
            seq[i]-=1
            seq[i+1]-=1
        if seq[i+1]!=0:
            return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    print moddable(int(raw_input()))
