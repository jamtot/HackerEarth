def hops(args):
    A,B,M = args[0],args[1],args[2]
    """hops=0
    for x in xrange(A,B+1):
        if x%M==0:
            hops+=1
    return hops""" #too slow
    if A%M==0: # if the first number divides evenly
        return ((B/M)-(A/M))+1
    else:
        return (B/M)-(A/M) 

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print hops(map(int,raw_input().split()))
