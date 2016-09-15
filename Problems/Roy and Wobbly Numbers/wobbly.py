def findwobbly(N,K):
    a,b=1,0
    for i in xrange(K-1):
        if b<9 and (b+1)!=a:
            b+=1
        elif b<8 and (b+1)==a:
            b+=2
        elif b==9 and a<9:
            b=0
            a+=1
        elif b==8 and a==9:
            return -1
    return ''.join(map(str,[a if i%2==0 else b for i in xrange(N)]))
            
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        NK = map(int, raw_input().split())
        print findwobbly(NK[0],NK[1])
