def findprod(N):
    A = map(int,raw_input().split())
    ans = 1
    for Ai in A:
        ans=(ans*Ai)%(10**9+7)
    return ans

if __name__ == "__main__":
    print findprod(int(raw_input()))
    
