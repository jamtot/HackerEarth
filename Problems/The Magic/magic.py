def stones(tocollect):
    stones = 0
    days = 0
    while stones < tocollect:
        tstones = 1
        while tstones*2 <= tocollect-stones:
            tstones*=2
        stones+=tstones
        days+=1
    return days

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print stones(int(raw_input()))
