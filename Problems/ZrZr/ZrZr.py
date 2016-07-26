#not used
def fac(N):
    if N==0: return 0
    elif N==1: return 1
    else:
        return N*fac(N-1)

def fives(N, Fs=0):
    while N>1:
        N/=5
        Fs+=N
    return Fs

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print fives(int(raw_input()))
