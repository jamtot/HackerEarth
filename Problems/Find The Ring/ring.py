def ring(start,moves):
    while moves > 0:
        if start == 0:
            start = 1
        elif start == 1:
            start = 0
        elif start == 2:
            start = 1
        moves-=1
    return start
        
if __name__ =="__main__":
    for tc in xrange(int(raw_input())):
        inp = map(int,raw_input().split())
        print ring(inp[0],inp[1])
