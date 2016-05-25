def maxRs(rkstr):
    lenstr = len(rkstr)
    # have to make one move, so a string of all R's
    # will end up with 1 K
    if lenstr == sum([1 for c in rkstr if c=='R']):
        return lenstr-1
    rs,curmax,maxR=0,0,0
    if rkstr[0]=='R':
        curmax=maxR=0
        rs+=1
    else:
        curmax=maxR=1
    for i in xrange(1,lenstr):
        if rkstr[i]=='R':
            rs+=1
            if curmax > 0:
                curmax-=1
        else:
            if curmax > 0: curmax+=1
            else: curmax = 1
        maxR = max(curmax,maxR)
    return maxR+rs    

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print maxRs(raw_input())
