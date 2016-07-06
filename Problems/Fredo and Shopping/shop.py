def shoppies(N): # not quite fast enough to get all inputs
    shops=map(int,raw_input().split())
    goto=[]
    for i in xrange(N):
        count=0
        for j in xrange(i):
            if (shops[i]>shops[j]):
                count+=1
        goto.append(count)
    return ' '.join(map(str, goto))

if __name__ == "__main__":
    print shoppies(int(raw_input()))        
