def iterations(n):
    calling=map(int,raw_input().split())
    ideal=map(int,raw_input().split())
    count=0
    for i in xrange(n):
        while calling[i]!=ideal[i]:
            temp=calling[i]
            for j in xrange(i,(n-1)):
                calling[j]=calling[j+1]
            calling[n-1]=temp
            count+=1
    return count+n

if __name__ == "__main__":
    print iterations(int(raw_input()))
