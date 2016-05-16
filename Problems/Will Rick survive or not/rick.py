def ricksurvive(walkers):
    W = map(int, raw_input().split())
    W.sort()
    i,j=0,1
    while i < walkers:
        if (W[i]-(j-1)) < 1:
            print "Goodbye Rick"
            print i
            break
        if j%7!=0:
            i+=1
        j+=1
    else:
        print "Rick now go and save Carl and Judas"
    

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        ricksurvive(int(raw_input()))
