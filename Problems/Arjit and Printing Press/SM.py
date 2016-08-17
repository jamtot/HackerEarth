def SuperMan(P, R):
    P=list(P)
    R=sorted(R)
    for i in xrange(len(P)):
        if len(R) > 0:
            if P[i]>R[0]:
                P[i]=R.pop(0)
    return ''.join(P)

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print SuperMan(raw_input(),raw_input())
