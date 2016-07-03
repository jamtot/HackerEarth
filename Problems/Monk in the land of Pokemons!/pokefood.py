def foodtobring(ponds):
    bring=0
    foods={}
    for p in xrange(ponds):
        A,B = map(int,raw_input().split())
        if A==B:
            continue
        foods.setdefault(A,0)
        foods.setdefault(B,0)
        foods[A]=foods[A]+1
        if foods[B]>0:
            foods[B]=foods[B]-1
        else:
            bring+=1
    return bring

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print foodtobring(int(raw_input()))
