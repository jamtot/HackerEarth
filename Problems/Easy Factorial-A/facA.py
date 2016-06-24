def fac(n):
    if n==1: return 1
    else: return n*fac(n-1)

def facA(n,m):
    return fac(n)%m

if __name__ == "__main__":
    nm=map(int,raw_input().split())
    print facA(nm[0],nm[1])
