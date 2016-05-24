def smallestdiff():
    deets = map(int, raw_input().split())
    studs = deets.pop(0)
    deets = sorted(deets)    
    pairs = []
    for i in xrange(studs/2):
        pairs.append(deets[i]+deets[(studs-1)-i])
    return max(pairs)-min(pairs)
        

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print smallestdiff()
