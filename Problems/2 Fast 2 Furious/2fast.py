def compareSpeeds(checkpoints):
    doms = map(int,raw_input().split())
    brians = map(int,raw_input().split())

    d_max,b_max = 0,0
    for i in xrange(checkpoints-1):
        d_change = abs(doms[i] - doms[i+1])
        b_change = abs(brians[i] - brians[i+1])
        if d_change > d_max:
            d_max = d_change
        if b_change > b_max:
            b_max = b_change
    max_change = max(d_max,b_max)
    out = ''
    if d_max > b_max:
        out="Dom"
    elif b_max > d_max:
        out="Brian"
    else:
        out="Tie"
    out+="\n%d"%max_change
    return out

if __name__ == "__main__":
    print compareSpeeds(int(raw_input()))
