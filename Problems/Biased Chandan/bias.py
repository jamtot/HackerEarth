def biasum__(n):
    ratings=[]
    cur = int(raw_input())
    for i in xrange(n-1):
        next=int(raw_input())
        if next!=0:
            ratings.append(cur)
        cur=next
    return sum(ratings)

def biasum(n): #gets rid of two previous to to zeros, this one passes problem
    ratings=[]
    for i in xrange(n):
        cur = int(raw_input())
        if cur==0:
            if len(ratings):
                ratings.pop()
        else:
            ratings.append(cur)
    return sum(ratings)

if __name__ == "__main__":
    print biasum(int(raw_input()))
