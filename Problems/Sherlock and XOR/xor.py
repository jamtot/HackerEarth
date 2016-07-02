def XORs(alen,array):
    """xors=0
    donedex=[]
    for i in xrange(alen):
        for j in xrange(1,alen):
            if (i!=j) and ((i,j) not in donedex):
                if (i^j)%2==1:
                    donedex.append((i,j))
                    donedex.append((j,i))
                    xors+=1"""
    evens = sum([1 if i%2==0 else 0 for i in array])
    return evens*(alen-evens)
    #too slow
    #return sum([1 if (array[i]^array[j])%2==1 else 0 for i in xrange(alen) for j in xrange(i+1, alen)])
    

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        alen = int(raw_input())
        array = map(int,raw_input().split())
        print XORs(alen,array)
