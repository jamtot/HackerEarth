def myfib(A,B,N):
    for i in xrange(N-1):
        A,B=B,A+B
    return A

if __name__ == "__main__":
    ABN = map(int,raw_input().split())
    print myfib(ABN[0],ABN[1],ABN[2])
