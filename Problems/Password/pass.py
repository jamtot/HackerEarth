def getpass(N):
    possibles = []
    newN = 0
    for i in xrange(N):
        newpossible = raw_input()
        if len(newpossible)%2==1:
            possibles.append(newpossible)
            newN+=1
    for i in xrange(newN):
        for j in xrange(newN):
            if i!=j:
                if possibles[i]==possibles[j][::-1]:
                    return "%d %s"%(len(possibles[i]), possibles[i][len(possibles[i])/2])

if __name__ == "__main__":
    N = int(raw_input())
    print getpass(N)
