def arrays(a1n, a2n):
    a1 = map(int,raw_input().split())
    a2 = map(int,raw_input().split())
    return " ".join(map(str,sorted(a1+a2, reverse=True)))

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        a1a2 = map(int, raw_input().split())
        print arrays(a1a2[0],a1a2[1])
