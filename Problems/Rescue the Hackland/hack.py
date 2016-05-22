def getgreys(inpt):
    L,R,K = inpt
    count=0
    while L<=R:
        count+=1
        L=L*K
        L+=1
    return count
    
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print getgreys(map(int,raw_input().split()))
