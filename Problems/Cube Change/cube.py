def scrape(N):
    if N>2:
        newN = N-2
        return (N**3)-(newN**3)
    else:
        return N**3

if __name__ == "__main__":  
    for tc in xrange(int(raw_input())):
        print scrape(int(raw_input()))
