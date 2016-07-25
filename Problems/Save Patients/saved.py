def saved(N):
    vaccines=sorted(map(int,raw_input().split()),reverse=True)
    mid=sorted(map(int,raw_input().split()),reverse=True)
    if all(mid[i]>vaccines[i] for i in xrange(N)):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    print saved(int(raw_input()))
