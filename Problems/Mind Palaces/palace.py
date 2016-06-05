# too slow for some testcases
def palace(NM):
    N,M = NM[0],NM[1]
    matrix = [raw_input().split() for i in xrange(N)]
    Q = int(raw_input())
    queries = [raw_input() for i in xrange(Q)]
    for q in queries:
        found = False
        for i in xrange(N):
            for j in xrange(M):
                if matrix[i][j] == q:
                    print i,j
                    found = True
                    break
            if found == True:
                break
        else:
            print -1,-1

def npalace(NM):
    # using 2d binary search
    N,M = NM[0],NM[1]
    matrix = [map(int,raw_input().split()) for i in xrange(N)]
    Q = int(raw_input())
    queries = [int(raw_input()) for i in xrange(Q)]
    for q in queries:
        i,j=0,M-1
        while i < N and j >= 0:
            if matrix[i][j] == q:
                print i,j
                break
            if matrix[i][j] > q:
                j-=1
            else:
                i+=1
        else:
            print -1,-1
    

if __name__ == "__main__":
    npalace(map(int,raw_input().split()))
