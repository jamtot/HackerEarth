def broken_dist(dist):
    """count=0
    for i in xrange(dist):
        if '3' not in str(i):
            count+=1
    return count"""
    #return len([i for i in xrange(dist) if '3' not in str(i)])
    count=0
    for i in xrange(dist):
        while i!=0:
            rem=i%10
            if rem==3: break
            i/=10
        else:
            count+=1
    return count

def next_num():
    count=0
    num=0
    mydict = {}
    while True:
        num+=1
        curnum=num
        while curnum!=0:
            rem=curnum%10
            if rem==3: break
            curnum/=10
        else:
            count+=1
        mydict[num]=count
        yield count, mydict
        
               
def dict_search(dist, dic):
    pass

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print broken_dist(int(raw_input()))
