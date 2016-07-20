def OLP(n):
    nA = map(int, raw_input().split())
    seq=[]
    j=0
    while j<3:
        seq.append(str(sum([nA[i] for i in xrange(j,n,3)])))
        j+=1
    return ' '.join(seq)

if __name__ == "__main__":
    print OLP(int(raw_input()))
