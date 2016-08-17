def maximum(S):
    mydict = {}
    S = sorted(S)
    for l in S:
        mydict.setdefault(l,0)
        mydict[l]+=1
    m=max(mydict, key=mydict.get)
    print m, mydict[m]

if __name__ == "__main__":
    maximum(raw_input())
