def divcount(lrk):
    l,r,k=lrk
    return sum([1 if i%k==0 and i/k>0 else 0 for i in xrange(l,r+1)])

if __name__ == "__main__":
    print divcount(map(int,raw_input().split()))
