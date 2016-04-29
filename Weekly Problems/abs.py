#T test cases
#N D number of ints, absolute diff to check
#N ints
#next N D
#next N ints

def test_case():
    ND = raw_input()
    N,D=map(int,ND.split())
    NARRAY = map(int, raw_input().split()[:N])
    if len(NARRAY)<2: return "YES"
    for i in xrange(len(NARRAY)-1):
        if abs(NARRAY[i]-NARRAY[i+1]) > D:
            return "NO"
    return "YES"

if __name__ == "__main__":
    T = int(raw_input())
    outputs=[]
    for i in xrange(T):
        print test_case()
