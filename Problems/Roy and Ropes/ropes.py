def ropeburn(L):
    uppers = map(int,raw_input().split())
    lowers = map(int,raw_input().split())
    curmax=L
    for i in xrange(1,L):
        curmax=max(curmax,i+uppers[i-1])
        curmax=max(curmax,i+lowers[i-1])
    return curmax

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print ropeburn(int(raw_input()))
