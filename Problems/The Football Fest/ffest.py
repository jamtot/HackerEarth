def passes(N, ID):
    prev=ID
    cur=ID
    for n in xrange(N):
        nPass = raw_input()
        if nPass[0] == 'B':
            prev,cur=cur,prev
        else:
            nPass=nPass.split()
            prev,cur=cur,nPass[1]
    return "Player %s"%cur
            

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        N,ID = raw_input().split()
        print passes(int(N), ID)
