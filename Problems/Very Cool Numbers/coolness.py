def dec_to_bin(x):
    return bin(x)[2:]

def cooliest(R,K):
    coolints=0
    for i in xrange(1,R+1):
        bini=dec_to_bin(i)
        coolness=0
        for j in xrange(len(bini)-2):
            if bini[j:j+3]=="101":
                coolness+=1
            if coolness>=K:
                coolints+=1
                break
    return coolints


if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        R,K=map(int,raw_input().split())
        print cooliest(R, K)
        
