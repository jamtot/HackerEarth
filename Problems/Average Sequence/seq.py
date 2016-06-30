def agetb(n):
    A,B=[],[]
    B=map(int,raw_input().split())
    for i in xrange(n):
        A.append((B[i]*(i+1))-sum(A[:i]))
    return " ".join(map(str,A))

if __name__ == "__main__":
    print agetb(int(raw_input()))
