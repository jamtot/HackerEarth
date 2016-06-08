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

def next_num_gen():
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
        yield num, mydict
        
               
def dict_search():
    mydict={}
    curmax = 0
    numgen = next_num_gen()
    
    for tc in xrange(int(raw_input())):
        #print broken_dist(int(raw_input()))
        num = int(raw_input())
        while curmax<num:
            curmax, mydict = numgen.next()
        print mydict
        print mydict[num]

def next_num_gen_list():
    count=0
    num=0
    mylist = []
    while True:
        num+=1
        curnum=num
        while curnum!=0:
            rem=curnum%10
            if rem==3: break
            curnum/=10
        else:
            count+=1
        mylist.append(count)
        yield num, mylist

def list_search():
    mylist=[]
    curmax = 0
    numgen = next_num_gen_list()
    
    for tc in xrange(int(raw_input())):
        #print broken_dist(int(raw_input()))
        num = int(raw_input())
        while curmax<num:
            curmax, mylist = numgen.next()
        #print mylist
        print mylist[num-1]

if __name__ == "__main__":
    #for tc in xrange(int(raw_input())):
        #print broken_dist(int(raw_input()))
    #dict_search() #too much memory used, slowing it down
    list_search()
