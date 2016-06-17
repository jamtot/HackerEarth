def reverse(n):
    n=str(n)
    if n==n[::-1]:
        return 1
    else:
        return 0

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        inp = map(int,raw_input().split())
        print sum([reverse(n) for n in xrange(inp[0],inp[1]+1)])
