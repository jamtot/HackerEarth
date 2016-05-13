def special():
    testcases = int(raw_input())
    for t in xrange(testcases):
        n = int(raw_input())
        mid = n/2 # half an odd integer is floored by truncation
        starpos = tuple()
        for i in xrange(n):
            line = raw_input()
            if '*' in line:
                starpos = (i,line.index('*'))
        print (abs(starpos[0]-mid)+abs(starpos[1]-mid))
    
if __name__ == "__main__":
    special()
