def evolving(pokemans):
    days=1
    curlongest = 0
    daymons = sorted(map(int,raw_input().split()), reverse=True)
    for i in xrange(pokemans):
        if daymons[i]>=curlongest:
            curlongest = daymons[i]
        else:
            curlongest-=1
        days+=1
    else:
        days+=curlongest
    return days

if __name__ == "__main__":
    print evolving(int(raw_input()))
        
