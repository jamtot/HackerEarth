def needed(args):
    N,M,X=args[0],args[1],args[2]
    A=map(int,raw_input().split())
    avg=0
    for i in xrange(N):
        avg+=A[i]
    needed=(X*(N+1))-avg
    if needed>M:
        return 'Impossible'
    else:
        return abs(needed)
    

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print needed(map(int,raw_input().split()))
